# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class CreateDataSetRequest(DaraModel):
    def __init__(
        self,
        data_set_description: str = None,
        data_set_field_key_name: str = None,
        data_set_file_name: str = None,
        data_set_name: str = None,
        data_set_status: int = None,
        data_set_type: str = None,
        ip_whitelist_recognizers: List[main_models.CreateDataSetRequestIpWhitelistRecognizers] = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The description of the dataset.
        self.data_set_description = data_set_description
        # The name of the unique key for the dataset.
        # 
        # This parameter is required.
        self.data_set_field_key_name = data_set_field_key_name
        # The name of the uploaded dataset file.
        # 
        # This parameter is required.
        self.data_set_file_name = data_set_file_name
        # The name of the dataset.
        # 
        # This parameter is required.
        self.data_set_name = data_set_name
        # The status of the dataset. Valid values:
        # 
        # - 0: deleted.
        # 
        # - 1: enabled.
        self.data_set_status = data_set_status
        # The type of the dataset. Valid values:
        # 
        # - custom: custom.
        # 
        # - preset: predefined.
        self.data_set_type = data_set_type
        # The list of recognizers.
        self.ip_whitelist_recognizers = ip_whitelist_recognizers
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The region of the Data Management center for threat analysis. Select a region based on where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: Your assets are outside China.
        self.region_id = region_id
        # The user ID of the member whose permissions are used to perform the operation. This parameter is used when an administrator acts on behalf of a member.
        self.role_for = role_for

    def validate(self):
        if self.ip_whitelist_recognizers:
            for v1 in self.ip_whitelist_recognizers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_description is not None:
            result['DataSetDescription'] = self.data_set_description

        if self.data_set_field_key_name is not None:
            result['DataSetFieldKeyName'] = self.data_set_field_key_name

        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status

        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type

        result['IpWhitelistRecognizers'] = []
        if self.ip_whitelist_recognizers is not None:
            for k1 in self.ip_whitelist_recognizers:
                result['IpWhitelistRecognizers'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetDescription') is not None:
            self.data_set_description = m.get('DataSetDescription')

        if m.get('DataSetFieldKeyName') is not None:
            self.data_set_field_key_name = m.get('DataSetFieldKeyName')

        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')

        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')

        self.ip_whitelist_recognizers = []
        if m.get('IpWhitelistRecognizers') is not None:
            for k1 in m.get('IpWhitelistRecognizers'):
                temp_model = main_models.CreateDataSetRequestIpWhitelistRecognizers()
                self.ip_whitelist_recognizers.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

class CreateDataSetRequestIpWhitelistRecognizers(DaraModel):
    def __init__(
        self,
        auto_recognize_status: str = None,
        ip_whitelist_recognizer_type: str = None,
        recognize_scope: str = None,
    ):
        # The automatic detection status. Valid values:
        # 
        # - enabled: enabled.
        # 
        # - disabled: disabled.
        self.auto_recognize_status = auto_recognize_status
        # The type of IP address that the recognizer detects. Valid values:
        # 
        # - sas_vulnerability_scanner_ip: The IP address of the Security Center web vulnerability scanner.
        # 
        # - waf_back_source_ip: The back-to-origin IP address of Web Application Firewall (WAF).
        # 
        # - ddos_back_source_ip: The back-to-origin IP address of Anti-DDoS.
        # 
        # - esa_back_source_ip: The back-to-origin IP address of an Edge Security Acceleration (ESA) node.
        # 
        # - ecs_public_ip: The public IP address of an Elastic Compute Service (ECS) instance.
        # 
        # - slb_public_ip: The public IP address of a Server Load Balancer (SLB) instance.
        # 
        # - vpc_eip: An Elastic IP Address (EIP).
        # 
        # - cdn_back_source_ip: The back-to-origin IP address of a content delivery network (CDN).
        # 
        # - ga_back_source_ip: The back-to-origin IP address of Global Accelerator (GA).
        self.ip_whitelist_recognizer_type = ip_whitelist_recognizer_type
        # The detection scope. Valid values:
        # 
        # - current_account: the current account only.
        # 
        # - rd_accounts: all accounts in your resource directory.
        self.recognize_scope = recognize_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recognize_status is not None:
            result['AutoRecognizeStatus'] = self.auto_recognize_status

        if self.ip_whitelist_recognizer_type is not None:
            result['IpWhitelistRecognizerType'] = self.ip_whitelist_recognizer_type

        if self.recognize_scope is not None:
            result['RecognizeScope'] = self.recognize_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecognizeStatus') is not None:
            self.auto_recognize_status = m.get('AutoRecognizeStatus')

        if m.get('IpWhitelistRecognizerType') is not None:
            self.ip_whitelist_recognizer_type = m.get('IpWhitelistRecognizerType')

        if m.get('RecognizeScope') is not None:
            self.recognize_scope = m.get('RecognizeScope')

        return self

