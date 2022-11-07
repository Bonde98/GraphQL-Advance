import graphene

from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class RegisterMutation(graphene.ObjectType):
    # Créer un utilisateur
    register = mutations.Register.Field()
    # Vérification d'un utilistaeur
    verify_account = mutations.VerifyAccount.Field()
    # Connecter d'un utilistaeur
    token_auth = mutations.ObtainJSONWebToken.Field()
    # Modifier un compte utilistaeur
    update_account = mutations.UpdateAccount.Field()
    # Renvoyer confirmation en email
    resend_activation_email = mutations.ResendActivationEmail.Field()
    
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(RegisterMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)