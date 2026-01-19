# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventLogPageRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        account_id_prp: str = None,
        begin_time: int = None,
        condition_1al: str = None,
        condition_2al: str = None,
        condition_3al: str = None,
        current_page: int = None,
        device_type_lrp: str = None,
        email_prp: str = None,
        end_time: int = None,
        fail_reason_lrp: str = None,
        ip_prp: str = None,
        login_result_arp: str = None,
        login_type_lrp: str = None,
        mac_prp: str = None,
        mobile_prp: str = None,
        nick_name_prp: str = None,
        operate_source_lrp: str = None,
        page_size: int = None,
        refer_prp: str = None,
        reg_id: str = None,
        register_ip_prp: str = None,
        req_id_pbs: str = None,
        score_ebs: int = None,
        score_sbs: int = None,
        service_abs: str = None,
        tags_lbs: str = None,
        umid_pdi: str = None,
        user_agent_prp: str = None,
        user_name_type_lrp: str = None,
    ):
        # Set the language type for request and response messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Account ID (request_param.accountId), up to 50 characters, supports “*” and “?” wildcards.
        self.account_id_prp = account_id_prp
        # Start timestamp of the log. Unit: milliseconds.
        self.begin_time = begin_time
        # Full-text match 1, cannot exceed 30 characters.
        self.condition_1al = condition_1al
        # Full-text match 2, cannot exceed 30 characters.
        self.condition_2al = condition_2al
        # Full-text match 3, cannot exceed 30 characters.
        self.condition_3al = condition_3al
        # Current page number.
        self.current_page = current_page
        # Device type (request_param.deviceType), examples: 1. PC, 2. MOBILE.
        self.device_type_lrp = device_type_lrp
        # Email (request_param.email), up to 100 characters, supports “*” and “?” wildcards.
        self.email_prp = email_prp
        # End time, accurate to milliseconds (ms).
        self.end_time = end_time
        # Login failure reason (-request_param.failReason).
        self.fail_reason_lrp = fail_reason_lrp
        # IP (request_param.ip), up to 20 characters, supports “*” and “?” wildcards.
        self.ip_prp = ip_prp
        # Login success indicator (request_param.loginResult).
        self.login_result_arp = login_result_arp
        # Login verification method (-request_param.loginType).
        self.login_type_lrp = login_type_lrp
        # Device MAC address (-request_param.mac), up to 30 characters, supports “*” and “?” wildcards.
        self.mac_prp = mac_prp
        # Phone number (supports MD5 request_param.mobile/request_param.mobileMd5), up to 30 characters, supports “*” and “?” wildcards, searchable by mobile and mobileMd5 fields.
        self.mobile_prp = mobile_prp
        # Account nickname (request_param.nickName), up to 50 characters, supports “*” and “?” wildcards.
        self.nick_name_prp = nick_name_prp
        # Operation source (request_param.operateSource), examples: 1. PC, 2. H5, 3. App.
        self.operate_source_lrp = operate_source_lrp
        # Number of items per page, default value is 10.
        self.page_size = page_size
        # Referer (-request_param.refer), up to 50 characters, supports “*” and “?” wildcards.
        self.refer_prp = refer_prp
        # Region code.
        self.reg_id = reg_id
        # Account registration IP (request_param.registerIp), up to 20 characters, supports “*” and “?” wildcards.
        self.register_ip_prp = register_ip_prp
        # Request ID.
        self.req_id_pbs = req_id_pbs
        # End value of the score range (score), only non-negative integers are allowed, and the right interval must be greater than the left interval, with both intervals being closed.
        self.score_ebs = score_ebs
        # Starting value of the score range (score), only non-negative integers are allowed, the right interval must be greater than the left interval, both intervals are inclusive.
        self.score_sbs = score_sbs
        # Event name (instance_id).
        self.service_abs = service_abs
        # Risk tags (tags), data source DescribeTagsList.
        self.tags_lbs = tags_lbs
        # Device ID (device_info.umid).
        self.umid_pdi = umid_pdi
        # User agent (-request_param.userAgent), up to 50 characters, supports “*” and “?” wildcards.
        self.user_agent_prp = user_agent_prp
        # Username type, login scenario (-request_param.userNameType).
        self.user_name_type_lrp = user_name_type_lrp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.account_id_prp is not None:
            result['accountIdPRP'] = self.account_id_prp

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.condition_1al is not None:
            result['condition1AL'] = self.condition_1al

        if self.condition_2al is not None:
            result['condition2AL'] = self.condition_2al

        if self.condition_3al is not None:
            result['condition3AL'] = self.condition_3al

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.device_type_lrp is not None:
            result['deviceTypeLRP'] = self.device_type_lrp

        if self.email_prp is not None:
            result['emailPRP'] = self.email_prp

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.fail_reason_lrp is not None:
            result['failReasonLRP'] = self.fail_reason_lrp

        if self.ip_prp is not None:
            result['ipPRP'] = self.ip_prp

        if self.login_result_arp is not None:
            result['loginResultARP'] = self.login_result_arp

        if self.login_type_lrp is not None:
            result['loginTypeLRP'] = self.login_type_lrp

        if self.mac_prp is not None:
            result['macPRP'] = self.mac_prp

        if self.mobile_prp is not None:
            result['mobilePRP'] = self.mobile_prp

        if self.nick_name_prp is not None:
            result['nickNamePRP'] = self.nick_name_prp

        if self.operate_source_lrp is not None:
            result['operateSourceLRP'] = self.operate_source_lrp

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.refer_prp is not None:
            result['referPRP'] = self.refer_prp

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.register_ip_prp is not None:
            result['registerIpPRP'] = self.register_ip_prp

        if self.req_id_pbs is not None:
            result['reqIdPBS'] = self.req_id_pbs

        if self.score_ebs is not None:
            result['scoreEBS'] = self.score_ebs

        if self.score_sbs is not None:
            result['scoreSBS'] = self.score_sbs

        if self.service_abs is not None:
            result['serviceABS'] = self.service_abs

        if self.tags_lbs is not None:
            result['tagsLBS'] = self.tags_lbs

        if self.umid_pdi is not None:
            result['umidPDI'] = self.umid_pdi

        if self.user_agent_prp is not None:
            result['userAgentPRP'] = self.user_agent_prp

        if self.user_name_type_lrp is not None:
            result['userNameTypeLRP'] = self.user_name_type_lrp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('accountIdPRP') is not None:
            self.account_id_prp = m.get('accountIdPRP')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('condition1AL') is not None:
            self.condition_1al = m.get('condition1AL')

        if m.get('condition2AL') is not None:
            self.condition_2al = m.get('condition2AL')

        if m.get('condition3AL') is not None:
            self.condition_3al = m.get('condition3AL')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('deviceTypeLRP') is not None:
            self.device_type_lrp = m.get('deviceTypeLRP')

        if m.get('emailPRP') is not None:
            self.email_prp = m.get('emailPRP')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('failReasonLRP') is not None:
            self.fail_reason_lrp = m.get('failReasonLRP')

        if m.get('ipPRP') is not None:
            self.ip_prp = m.get('ipPRP')

        if m.get('loginResultARP') is not None:
            self.login_result_arp = m.get('loginResultARP')

        if m.get('loginTypeLRP') is not None:
            self.login_type_lrp = m.get('loginTypeLRP')

        if m.get('macPRP') is not None:
            self.mac_prp = m.get('macPRP')

        if m.get('mobilePRP') is not None:
            self.mobile_prp = m.get('mobilePRP')

        if m.get('nickNamePRP') is not None:
            self.nick_name_prp = m.get('nickNamePRP')

        if m.get('operateSourceLRP') is not None:
            self.operate_source_lrp = m.get('operateSourceLRP')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('referPRP') is not None:
            self.refer_prp = m.get('referPRP')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('registerIpPRP') is not None:
            self.register_ip_prp = m.get('registerIpPRP')

        if m.get('reqIdPBS') is not None:
            self.req_id_pbs = m.get('reqIdPBS')

        if m.get('scoreEBS') is not None:
            self.score_ebs = m.get('scoreEBS')

        if m.get('scoreSBS') is not None:
            self.score_sbs = m.get('scoreSBS')

        if m.get('serviceABS') is not None:
            self.service_abs = m.get('serviceABS')

        if m.get('tagsLBS') is not None:
            self.tags_lbs = m.get('tagsLBS')

        if m.get('umidPDI') is not None:
            self.umid_pdi = m.get('umidPDI')

        if m.get('userAgentPRP') is not None:
            self.user_agent_prp = m.get('userAgentPRP')

        if m.get('userNameTypeLRP') is not None:
            self.user_name_type_lrp = m.get('userNameTypeLRP')

        return self

