from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    input_description = models.TextField()
    input = models.TextField()
    output_description = models.TextField()
    output = models.TextField()

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"


class Submission(models.Model):
    class ProgrammingLanguage(models.TextChoices):
        C99 = "C99"
        CXX11 = "C++11"
        PYTHON3 = "Python 3.10.5"

    class SubmissionStatus(models.TextChoices):
        PENDING = "PENDING"
        RUNNING = "RUNNING"
        PASSED = "PASSED"
        FAILED = "FAILED"

    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(
        max_length=max(map(lambda x: len(x), ProgrammingLanguage.values)),
        choices=ProgrammingLanguage.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=max(map(lambda x: len(x), SubmissionStatus.values)),
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.PENDING,
    )

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.problem_id} "
            f"(lang={self.language}, created_at={self.created_at}, status={self.status})"
        )
