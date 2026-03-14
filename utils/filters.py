from telegram.ext import filters
from config import ADMIN_ID

class AdminFilter(filters.MessageFilter):
    def filter(self, message):
        return message.from_user.id == ADMIN_ID

# Instance to use in handlers
is_admin = AdminFilter()
