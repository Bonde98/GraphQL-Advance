import graphene
from graphene_django import DjangoObjectType, DjangoListField

from .models import Category, Question, Quizzes, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','name')
    
class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id','title','category','date_created')

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('id','quiz','title','difficulty','technique','is_active')
        
    
class AnswerType(DjangoObjectType):
    
    class Meta:
        model = Answer
        fields = ('id','answer_text','question','is_right')
        
class Query(graphene.ObjectType):
    
    all_category = graphene.List(CategoryType,id=graphene.Int())
    all_quizzes = DjangoListField(QuizzesType)
    
    
    
    def resolve_all_category(root, info, id):
        return Category.objects.get(pk=id)
    
    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    
    
#Créer un Categorie    
class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        
    category = graphene.Field(CategoryType)
    
    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)

#Modifier un Categorie
class UpdateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()
        
    category = graphene.Field(CategoryType)
    
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        return UpdateCategory(category=category)
    
#Supprimer un Categorie
class DeletCategory(graphene.Mutation):
    class Arguments:
        
        id = graphene.ID()
        
    category = graphene.Field(CategoryType)
    
    def mutate(cls, root, info, id):
        category = Category.objects.get(pk=id)
       
        category.delete()
        return UpdateCategory(category=category)
        
class QuizzesInput(graphene.InputObjectType):
   title = graphene.String()
   category = graphene.String()
   date_created = graphene.Int()

#Créer un Quizzes   
class CreateQuizzes(graphene.Mutation):
    class Arguments:
        input = QuizzesInput(required=True)
        
    quizzes = graphene.Field(QuizzesType)
    
    @classmethod
    def mutate(cls, root, info, input):
        quizzes = Quizzes()
        quizzes.title = input.title
        quizzes.category = input.category
        quizzes.date_created = input.date_created
        
        return CreateQuizzes(quizzes=quizzes)

#Modifier un Quizzes   
class UpdateQuizzes(graphene.Mutation):
    class Arguments:
        input = QuizzesInput(required=True)
        id = graphene.ID()
        
    quizzes = graphene.Field(QuizzesType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        quizzes = Quizzes.objects.get(id=id)
        quizzes.title = input.title
        quizzes.category = input.category
        quizzes.date_created = input.date_created
        quizzes.save()
        
        return UpdateQuizzes(quizzes=quizzes)

#Supprimer un Quizzes   
class DeleteQuizzes(graphene.Mutation):
    class Arguments:    
        id = graphene.ID()
        
    quizzes = graphene.Field(QuizzesType)
    
    @classmethod
    def mutate(cls, root, info, id):
        quizzes = Quizzes.objects.get(id=id)
        quizzes.delete()
        
        return DeleteQuizzes(quizzes=quizzes)

class QuestionInput(graphene.InputObjectType):
    quiz = graphene.String()
    title = graphene.String()
    difficulty = graphene.String()
    technique = graphene.String()
    is_active = graphene.Boolean()

# Créer Question
class CreateQuestion(graphene.Mutation):
    class Arguments:
        input = QuestionInput(required=True)
        
    question = graphene.Field(QuestionType)
    def mutate(cls, root, info, input):
        question = Question()
        question.quiz = input.quiz
        question.difficulty = input.difficulty
        question.technique = input.technique
        question.is_active = input.is_active
        return CreateQuestion(question=question)

#Modifier un Quizzes   
class UpdateQuestion(graphene.Mutation):
    class Arguments:
        input = QuestionInput(required=True)
        id = graphene.ID()
        
    question = graphene.Field(QuestionType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        question = Quizzes.objects.get(id=id)
        question.title = input.title
        question.category = input.category
        question.date_created = input.date_created
        question.save()
        
        return UpdateQuestion(question=question)

#Supprimer un Quizzes   
class DeleteQuestion(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    question = graphene.Field(QuizzesType)
    
    @classmethod
    def mutate(cls, root, info, id):
        question = Quizzes.objects.get(id=id)
        question.delete()
        
        return DeleteQuestion(question=question)


class AnswerInput(graphene.InputObjectType):
    answer_text = graphene.String()
    question = graphene.String()
    is_right = graphene.Boolean()
 
# Créer Answer   
class CreateAnswer(graphene.Mutation):
    class Arguments:
        input = AnswerInput(required=True)
    
    answer = graphene.Field(AnswerType)
    def mutate(cls, root, info, input):
        answer = Answer()
        answer.answer_text = input.answer_text
        answer.question = input.question
        answer.is_right = input.is_right
        return CreateAnswer(answer=answer)

#Modifier un Answer   
class UpdateAnswer(graphene.Mutation):
    class Arguments:
        input = AnswerInput(required=True)
        id = graphene.ID()
        
    answer = graphene.Field(QuestionType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        answer = Answer.objects.get(id=id)
        answer.answer_text = input.answer_text
        answer.question = input.questin
        answer.is_right = input.is_right
        answer.save()
        
        return UpdateAnswer(answer=answer)

#Supprimer un Answer   
class DeleteAnswer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    answer = graphene.Field(AnswerType)
    
    @classmethod
    def mutate(cls, root, info, id):
        answer = Answer.objects.get(id=id)
        answer.delete()
        
        return DeleteAnswer(answer=answer)




class Mutation(graphene.ObjectType):
    # CRUD des Catégories
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeletCategory.Field()
     # CRUD des Quizzes
    create_quizzes = CreateQuizzes.Field()
    update_quizzes = UpdateQuizzes.Field()
    delete_quizzes = DeleteQuizzes.Field()
    # CRUD des Questions
    create_question = CreateQuestion.Field()
    update_question = UpdateQuestion.Field()
    delete_question = DeleteQuestion.Field()
     # CRUD des Answer
    create_answer = CreateAnswer.Field()
    update_answer= UpdateAnswer.Field()
    delete_answer = DeleteAnswer.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)