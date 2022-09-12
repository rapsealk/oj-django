import graphene

import onlinejudge.problems.schema


class Query(
    onlinejudge.problems.schema.Query,
    graphene.ObjectType,  # type: ignore
):
    pass


schema = graphene.Schema(query=Query, mutation=onlinejudge.problems.schema.Mutation)
