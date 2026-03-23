# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescAccountSummaryResponseBody(DaraModel):
    def __init__(
        self,
        daily_quota: int = None,
        daily_remain_free_quota: int = None,
        dayu_status: int = None,
        domains: int = None,
        enable_times: int = None,
        ip_channel_type: str = None,
        mail_addresses: int = None,
        max_quota_level: int = None,
        month_quota: int = None,
        quota_level: int = None,
        receivers: int = None,
        remain_free_quota: int = None,
        request_id: str = None,
        sms_record: int = None,
        sms_sign: int = None,
        sms_templates: int = None,
        tags: int = None,
        templates: int = None,
        user_status: int = None,
    ):
        # The daily quota.
        self.daily_quota = daily_quota
        # The remaining daily free quota.
        self.daily_remain_free_quota = daily_remain_free_quota
        # The status of Dayu. This parameter is deprecated and retained for compatibility.
        self.dayu_status = dayu_status
        # The number of domain names.
        self.domains = domains
        # The effective period.
        self.enable_times = enable_times
        # The type of the outbound IP channel.
        # 
        # 1. backup: A backup IP channel that is not actively maintained. Customers using this channel are advised to purchase a dedicated IP for better stability.
        # 
        # 2. normal: A normal IP channel that is continuously maintained by the email delivery team to ensure stable and reliable service.
        self.ip_channel_type = ip_channel_type
        # The number of sender addresses.
        self.mail_addresses = mail_addresses
        # The maximum reputation level.
        self.max_quota_level = max_quota_level
        # The monthly quota.
        self.month_quota = month_quota
        # The reputation level.
        self.quota_level = quota_level
        # The number of recipients.
        self.receivers = receivers
        # The remaining free quota.
        self.remain_free_quota = remain_free_quota
        # The request ID.
        self.request_id = request_id
        # This parameter is deprecated. It is retained for compatibility.
        self.sms_record = sms_record
        # This parameter is deprecated. It is retained for compatibility.
        self.sms_sign = sms_sign
        # This parameter is deprecated. It is retained for compatibility.
        self.sms_templates = sms_templates
        # The number of tags.
        self.tags = tags
        # The number of templates.
        self.templates = templates
        # The status of the user. Valid values: 0: Normal. 1: Freeze. 2: Overdue payment. 4: Outbound messages are restricted. 8: The user is logically deleted.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_quota is not None:
            result['DailyQuota'] = self.daily_quota

        if self.daily_remain_free_quota is not None:
            result['DailyRemainFreeQuota'] = self.daily_remain_free_quota

        if self.dayu_status is not None:
            result['DayuStatus'] = self.dayu_status

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.enable_times is not None:
            result['EnableTimes'] = self.enable_times

        if self.ip_channel_type is not None:
            result['IpChannelType'] = self.ip_channel_type

        if self.mail_addresses is not None:
            result['MailAddresses'] = self.mail_addresses

        if self.max_quota_level is not None:
            result['MaxQuotaLevel'] = self.max_quota_level

        if self.month_quota is not None:
            result['MonthQuota'] = self.month_quota

        if self.quota_level is not None:
            result['QuotaLevel'] = self.quota_level

        if self.receivers is not None:
            result['Receivers'] = self.receivers

        if self.remain_free_quota is not None:
            result['RemainFreeQuota'] = self.remain_free_quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sms_record is not None:
            result['SmsRecord'] = self.sms_record

        if self.sms_sign is not None:
            result['SmsSign'] = self.sms_sign

        if self.sms_templates is not None:
            result['SmsTemplates'] = self.sms_templates

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.templates is not None:
            result['Templates'] = self.templates

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyQuota') is not None:
            self.daily_quota = m.get('DailyQuota')

        if m.get('DailyRemainFreeQuota') is not None:
            self.daily_remain_free_quota = m.get('DailyRemainFreeQuota')

        if m.get('DayuStatus') is not None:
            self.dayu_status = m.get('DayuStatus')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('EnableTimes') is not None:
            self.enable_times = m.get('EnableTimes')

        if m.get('IpChannelType') is not None:
            self.ip_channel_type = m.get('IpChannelType')

        if m.get('MailAddresses') is not None:
            self.mail_addresses = m.get('MailAddresses')

        if m.get('MaxQuotaLevel') is not None:
            self.max_quota_level = m.get('MaxQuotaLevel')

        if m.get('MonthQuota') is not None:
            self.month_quota = m.get('MonthQuota')

        if m.get('QuotaLevel') is not None:
            self.quota_level = m.get('QuotaLevel')

        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')

        if m.get('RemainFreeQuota') is not None:
            self.remain_free_quota = m.get('RemainFreeQuota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmsRecord') is not None:
            self.sms_record = m.get('SmsRecord')

        if m.get('SmsSign') is not None:
            self.sms_sign = m.get('SmsSign')

        if m.get('SmsTemplates') is not None:
            self.sms_templates = m.get('SmsTemplates')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Templates') is not None:
            self.templates = m.get('Templates')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

