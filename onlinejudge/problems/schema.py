from typing import Any, Iterable

import graphene
from graphene_django import DjangoObjectType

from .models import Problem, Submission


class ProblemType(DjangoObjectType):  # type: ignore
    class Meta:
        model = Problem
        fields = (
            "id",
            "title",
            "description",
            "input_description",
            "input",
            "output_description",
            "output",
        )


class SubmissionType(DjangoObjectType):  # type: ignore
    class Meta:
        model = Submission
        fields = ("id", "problem_id", "code", "language", "created_at", "status")


class Query:
    problems = graphene.List(ProblemType)
    submissions = graphene.List(SubmissionType)

    def resolve_problems(root: "Query", info: Any) -> Iterable[Problem]:
        # We can easily optimize query count in the resolve method
        return Problem.objects.all()

    def resolve_submissions(root: "Query", info: Any) -> Iterable[Submission]:
        """
        query {
            submissions {
                id
                problemId {
                    id
                    title
                }
                # language
                code
                createdAt
            }
        }
        """
        return Submission.objects.all()


class CreateSubmission(graphene.Mutation):
    class Arguments:
        problem_id = graphene.Int()
        code = graphene.String()
        language = graphene.String()

    ok = graphene.Boolean()
    submission = graphene.Field(SubmissionType)

    def mutate(root: "Query", info: Any, problem_id: int, code: str, language: str) -> "CreateSubmission":
        """
        mutation CreateSubmission {
            createSubmission(problemId: 1, code: "print('hi')", language: "python") {
                submission {
                    id
                    code
                }
                ok
            }
        }
        """
        problem = Problem.objects.filter(id=problem_id).first()
        submission = Submission(problem_id=problem, code=code, language=language)
        submission.save()
        ok = True
        return CreateSubmission(ok=ok, submission=submission)


class Mutation(graphene.ObjectType):
    create_submission = CreateSubmission.Field()
