class KnowledgeService:
    def __init__(self, knowledge_repo):
        self.knowledge_repo = knowledge_repo

    def get_knowledge(self, knowledge_id):
        return self.knowledge_repo.get(knowledge_id)

    def create_knowledge(self, knowledge):
        return self.knowledge_repo.create(knowledge)

 