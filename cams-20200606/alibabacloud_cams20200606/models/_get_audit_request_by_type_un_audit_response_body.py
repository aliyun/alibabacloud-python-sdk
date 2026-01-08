# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetAuditRequestByTypeUnAuditResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetAuditRequestByTypeUnAuditResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAuditRequestByTypeUnAuditResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAuditRequestByTypeUnAuditResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        audit_record: main_models.GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecord = None,
        audit_result: str = None,
        audit_time: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modifier: str = None,
        id: str = None,
        maap_service_no: str = None,
        modifier: str = None,
        request_no: str = None,
        request_type: str = None,
        state: str = None,
        subscriber_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.audit_record = audit_record
        self.audit_result = audit_result
        self.audit_time = audit_time
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modifier = gmt_modifier
        # ID
        self.id = id
        self.maap_service_no = maap_service_no
        self.modifier = modifier
        self.request_no = request_no
        self.request_type = request_type
        self.state = state
        self.subscriber_code = subscriber_code

    def validate(self):
        if self.audit_record:
            self.audit_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.audit_record is not None:
            result['AuditRecord'] = self.audit_record.to_map()

        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modifier is not None:
            result['GmtModifier'] = self.gmt_modifier

        if self.id is not None:
            result['Id'] = self.id

        if self.maap_service_no is not None:
            result['MaapServiceNo'] = self.maap_service_no

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.request_no is not None:
            result['RequestNo'] = self.request_no

        if self.request_type is not None:
            result['RequestType'] = self.request_type

        if self.state is not None:
            result['State'] = self.state

        if self.subscriber_code is not None:
            result['SubscriberCode'] = self.subscriber_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AuditRecord') is not None:
            temp_model = main_models.GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecord()
            self.audit_record = temp_model.from_map(m.get('AuditRecord'))

        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModifier') is not None:
            self.gmt_modifier = m.get('GmtModifier')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaapServiceNo') is not None:
            self.maap_service_no = m.get('MaapServiceNo')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('RequestNo') is not None:
            self.request_no = m.get('RequestNo')

        if m.get('RequestType') is not None:
            self.request_type = m.get('RequestType')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SubscriberCode') is not None:
            self.subscriber_code = m.get('SubscriberCode')

        return self

class GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecord(DaraModel):
    def __init__(
        self,
        age_limit: str = None,
        apply_reason: str = None,
        business_account_name: str = None,
        company_address: List[main_models.GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecordCompanyAddress] = None,
        company_english_name: str = None,
        company_legal_name: str = None,
        company_legal_person: str = None,
        company_profile: str = None,
        company_registered_country: List[str] = None,
        company_tel: List[main_models.GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecordCompanyTel] = None,
        contact_mail: str = None,
        enable_auto_reply: str = None,
        industry_description: str = None,
        industry_involved: str = None,
        letter_guarantee: str = None,
        logo: List[str] = None,
        message_destination_country: List[str] = None,
        message_destination_international_country: List[str] = None,
        message_dialogue_introduction: str = None,
        message_enable_date: str = None,
        message_session_name: str = None,
        now_recovery: str = None,
        recovery_date: str = None,
        reply_content: str = None,
        suspension_date: str = None,
        web_address: str = None,
    ):
        self.age_limit = age_limit
        self.apply_reason = apply_reason
        self.business_account_name = business_account_name
        self.company_address = company_address
        self.company_english_name = company_english_name
        self.company_legal_name = company_legal_name
        self.company_legal_person = company_legal_person
        self.company_profile = company_profile
        self.company_registered_country = company_registered_country
        self.company_tel = company_tel
        self.contact_mail = contact_mail
        self.enable_auto_reply = enable_auto_reply
        self.industry_description = industry_description
        self.industry_involved = industry_involved
        self.letter_guarantee = letter_guarantee
        self.logo = logo
        self.message_destination_country = message_destination_country
        self.message_destination_international_country = message_destination_international_country
        self.message_dialogue_introduction = message_dialogue_introduction
        self.message_enable_date = message_enable_date
        self.message_session_name = message_session_name
        self.now_recovery = now_recovery
        self.recovery_date = recovery_date
        self.reply_content = reply_content
        # SuspensionDate
        self.suspension_date = suspension_date
        self.web_address = web_address

    def validate(self):
        if self.company_address:
            for v1 in self.company_address:
                 if v1:
                    v1.validate()
        if self.company_tel:
            for v1 in self.company_tel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.age_limit is not None:
            result['AgeLimit'] = self.age_limit

        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason

        if self.business_account_name is not None:
            result['BusinessAccountName'] = self.business_account_name

        result['CompanyAddress'] = []
        if self.company_address is not None:
            for k1 in self.company_address:
                result['CompanyAddress'].append(k1.to_map() if k1 else None)

        if self.company_english_name is not None:
            result['CompanyEnglishName'] = self.company_english_name

        if self.company_legal_name is not None:
            result['CompanyLegalName'] = self.company_legal_name

        if self.company_legal_person is not None:
            result['CompanyLegalPerson'] = self.company_legal_person

        if self.company_profile is not None:
            result['CompanyProfile'] = self.company_profile

        if self.company_registered_country is not None:
            result['CompanyRegisteredCountry'] = self.company_registered_country

        result['CompanyTel'] = []
        if self.company_tel is not None:
            for k1 in self.company_tel:
                result['CompanyTel'].append(k1.to_map() if k1 else None)

        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail

        if self.enable_auto_reply is not None:
            result['EnableAutoReply'] = self.enable_auto_reply

        if self.industry_description is not None:
            result['IndustryDescription'] = self.industry_description

        if self.industry_involved is not None:
            result['IndustryInvolved'] = self.industry_involved

        if self.letter_guarantee is not None:
            result['LetterGuarantee'] = self.letter_guarantee

        if self.logo is not None:
            result['Logo'] = self.logo

        if self.message_destination_country is not None:
            result['MessageDestinationCountry'] = self.message_destination_country

        if self.message_destination_international_country is not None:
            result['MessageDestinationInternationalCountry'] = self.message_destination_international_country

        if self.message_dialogue_introduction is not None:
            result['MessageDialogueIntroduction'] = self.message_dialogue_introduction

        if self.message_enable_date is not None:
            result['MessageEnableDate'] = self.message_enable_date

        if self.message_session_name is not None:
            result['MessageSessionName'] = self.message_session_name

        if self.now_recovery is not None:
            result['NowRecovery'] = self.now_recovery

        if self.recovery_date is not None:
            result['RecoveryDate'] = self.recovery_date

        if self.reply_content is not None:
            result['ReplyContent'] = self.reply_content

        if self.suspension_date is not None:
            result['SuspensionDate'] = self.suspension_date

        if self.web_address is not None:
            result['WebAddress'] = self.web_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgeLimit') is not None:
            self.age_limit = m.get('AgeLimit')

        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')

        if m.get('BusinessAccountName') is not None:
            self.business_account_name = m.get('BusinessAccountName')

        self.company_address = []
        if m.get('CompanyAddress') is not None:
            for k1 in m.get('CompanyAddress'):
                temp_model = main_models.GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecordCompanyAddress()
                self.company_address.append(temp_model.from_map(k1))

        if m.get('CompanyEnglishName') is not None:
            self.company_english_name = m.get('CompanyEnglishName')

        if m.get('CompanyLegalName') is not None:
            self.company_legal_name = m.get('CompanyLegalName')

        if m.get('CompanyLegalPerson') is not None:
            self.company_legal_person = m.get('CompanyLegalPerson')

        if m.get('CompanyProfile') is not None:
            self.company_profile = m.get('CompanyProfile')

        if m.get('CompanyRegisteredCountry') is not None:
            self.company_registered_country = m.get('CompanyRegisteredCountry')

        self.company_tel = []
        if m.get('CompanyTel') is not None:
            for k1 in m.get('CompanyTel'):
                temp_model = main_models.GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecordCompanyTel()
                self.company_tel.append(temp_model.from_map(k1))

        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')

        if m.get('EnableAutoReply') is not None:
            self.enable_auto_reply = m.get('EnableAutoReply')

        if m.get('IndustryDescription') is not None:
            self.industry_description = m.get('IndustryDescription')

        if m.get('IndustryInvolved') is not None:
            self.industry_involved = m.get('IndustryInvolved')

        if m.get('LetterGuarantee') is not None:
            self.letter_guarantee = m.get('LetterGuarantee')

        if m.get('Logo') is not None:
            self.logo = m.get('Logo')

        if m.get('MessageDestinationCountry') is not None:
            self.message_destination_country = m.get('MessageDestinationCountry')

        if m.get('MessageDestinationInternationalCountry') is not None:
            self.message_destination_international_country = m.get('MessageDestinationInternationalCountry')

        if m.get('MessageDialogueIntroduction') is not None:
            self.message_dialogue_introduction = m.get('MessageDialogueIntroduction')

        if m.get('MessageEnableDate') is not None:
            self.message_enable_date = m.get('MessageEnableDate')

        if m.get('MessageSessionName') is not None:
            self.message_session_name = m.get('MessageSessionName')

        if m.get('NowRecovery') is not None:
            self.now_recovery = m.get('NowRecovery')

        if m.get('RecoveryDate') is not None:
            self.recovery_date = m.get('RecoveryDate')

        if m.get('ReplyContent') is not None:
            self.reply_content = m.get('ReplyContent')

        if m.get('SuspensionDate') is not None:
            self.suspension_date = m.get('SuspensionDate')

        if m.get('WebAddress') is not None:
            self.web_address = m.get('WebAddress')

        return self

class GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecordCompanyTel(DaraModel):
    def __init__(
        self,
        company_tel_number: str = None,
        company_tel_title: str = None,
    ):
        self.company_tel_number = company_tel_number
        self.company_tel_title = company_tel_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_tel_number is not None:
            result['CompanyTelNumber'] = self.company_tel_number

        if self.company_tel_title is not None:
            result['CompanyTelTitle'] = self.company_tel_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyTelNumber') is not None:
            self.company_tel_number = m.get('CompanyTelNumber')

        if m.get('CompanyTelTitle') is not None:
            self.company_tel_title = m.get('CompanyTelTitle')

        return self

class GetAuditRequestByTypeUnAuditResponseBodyDataAuditRecordCompanyAddress(DaraModel):
    def __init__(
        self,
        company_address: str = None,
        company_address_title: str = None,
    ):
        self.company_address = company_address
        self.company_address_title = company_address_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_address is not None:
            result['CompanyAddress'] = self.company_address

        if self.company_address_title is not None:
            result['CompanyAddressTitle'] = self.company_address_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyAddress') is not None:
            self.company_address = m.get('CompanyAddress')

        if m.get('CompanyAddressTitle') is not None:
            self.company_address_title = m.get('CompanyAddressTitle')

        return self

