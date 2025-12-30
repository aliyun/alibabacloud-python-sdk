# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateDnsGtmInstanceGlobalConfigRequest(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.UpdateDnsGtmInstanceGlobalConfigRequestAlertConfig] = None,
        alert_group: str = None,
        cname_type: str = None,
        force_update: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        lang: str = None,
        public_cname_mode: str = None,
        public_rr: str = None,
        public_user_domain_name: str = None,
        public_zone_name: str = None,
        ttl: int = None,
    ):
        self.alert_config = alert_config
        # The name of the alert group in the JSON format.
        self.alert_group = alert_group
        # The type of the canonical name (CNAME).
        # 
        # *   Set the value to PUBLIC.
        self.cname_type = cname_type
        # Specifies whether to enable force updates. Valid values:
        # 
        # *   true: enables force update without a conflict alert.
        # *   false: disables force update. If a conflict occurs, the system displays an alert. null: This valid value of ForceUpdate provides the same information as the false value.
        self.force_update = force_update
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the instance. This parameter is required only for the first update.
        self.instance_name = instance_name
        # The language of the values of specific response parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # Specifies whether to use a custom CNAME domain name or a CNAME domain name assigned by the system to access the instance over the Internet. Valid values:
        # 
        # *   SYSTEM_ASSIGN: a CNAME domain name assigned by the system
        # *   CUSTOM: a custom CNAME domain name
        self.public_cname_mode = public_cname_mode
        # The hostname corresponding to the CNAME domain name that is used to access the instance over the Internet.
        self.public_rr = public_rr
        # The service domain name that is used over the Internet.
        self.public_user_domain_name = public_user_domain_name
        # The CNAME domain name that is used to access the instance over the Internet, which is the primary domain name. This parameter is required when the PublicCnameMode parameter is set to CUSTOM.
        # 
        # >  You must use the primary domain name. Do not include the hostname specified by the PublicRr parameter.
        self.public_zone_name = public_zone_name
        # The global time to live (TTL).
        self.ttl = ttl

    def validate(self):
        if self.alert_config:
            for v1 in self.alert_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k1 in self.alert_config:
                result['AlertConfig'].append(k1.to_map() if k1 else None)

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.cname_type is not None:
            result['CnameType'] = self.cname_type

        if self.force_update is not None:
            result['ForceUpdate'] = self.force_update

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.public_cname_mode is not None:
            result['PublicCnameMode'] = self.public_cname_mode

        if self.public_rr is not None:
            result['PublicRr'] = self.public_rr

        if self.public_user_domain_name is not None:
            result['PublicUserDomainName'] = self.public_user_domain_name

        if self.public_zone_name is not None:
            result['PublicZoneName'] = self.public_zone_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.UpdateDnsGtmInstanceGlobalConfigRequestAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('CnameType') is not None:
            self.cname_type = m.get('CnameType')

        if m.get('ForceUpdate') is not None:
            self.force_update = m.get('ForceUpdate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PublicCnameMode') is not None:
            self.public_cname_mode = m.get('PublicCnameMode')

        if m.get('PublicRr') is not None:
            self.public_rr = m.get('PublicRr')

        if m.get('PublicUserDomainName') is not None:
            self.public_user_domain_name = m.get('PublicUserDomainName')

        if m.get('PublicZoneName') is not None:
            self.public_zone_name = m.get('PublicZoneName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class UpdateDnsGtmInstanceGlobalConfigRequestAlertConfig(DaraModel):
    def __init__(
        self,
        dingtalk_notice: bool = None,
        email_notice: bool = None,
        notice_type: str = None,
        sms_notice: bool = None,
    ):
        self.dingtalk_notice = dingtalk_notice
        self.email_notice = email_notice
        self.notice_type = notice_type
        self.sms_notice = sms_notice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dingtalk_notice is not None:
            result['DingtalkNotice'] = self.dingtalk_notice

        if self.email_notice is not None:
            result['EmailNotice'] = self.email_notice

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        if self.sms_notice is not None:
            result['SmsNotice'] = self.sms_notice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingtalkNotice') is not None:
            self.dingtalk_notice = m.get('DingtalkNotice')

        if m.get('EmailNotice') is not None:
            self.email_notice = m.get('EmailNotice')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('SmsNotice') is not None:
            self.sms_notice = m.get('SmsNotice')

        return self

