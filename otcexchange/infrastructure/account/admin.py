from django.contrib import admin
from .models import DefaultLevels, UserLevel, UserBankInfo, UserAuthInfo
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone_number")

class DefaultLevelsAdmin(admin.ModelAdmin):
    list_display = ("id", "level", "convert" ,"deposit_irr" ,"deposit_crypto",
                     "withdraw_irr", "withdraw_crypto", "buy", "sell", "turnover")

class UserLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "level", "convert" ,"deposit_irr" ,"deposit_crypto",
                     "withdraw_irr", "withdraw_crypto", "buy", "sell", "turnover")

class UserBankInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "account_card_number", "iban")

class UserAuthInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "kyc_completed", "kyc_verified", "nation_code", "father_name", "card_image",
                     "backside_card_image", "verification_video", "gender", "job", "approximate_monthly_deposit")


admin.site.register(User, UserAdmin)    
admin.site.register(DefaultLevels, DefaultLevelsAdmin)  
admin.site.register(UserLevel, UserLevelAdmin)  
admin.site.register(UserBankInfo, UserBankInfoAdmin)  
admin.site.register(UserAuthInfo, UserAuthInfoAdmin)  
