# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetNacosConfigResponseBody(DaraModel):
    def __init__(
        self,
        configuration: main_models.GetNacosConfigResponseBodyConfiguration = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Configuration information.
        self.configuration = configuration
        # Error code.
        self.error_code = error_code
        # Message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # The result of the request, with values as follows:
        # - `true`: The request was successful.
        # - `false`: The request failed.
        self.success = success

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            temp_model = main_models.GetNacosConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m.get('Configuration'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNacosConfigResponseBodyConfiguration(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        beta_ips: str = None,
        content: str = None,
        data_id: str = None,
        desc: str = None,
        encrypted_data_key: str = None,
        gray_versions: List[main_models.GetNacosConfigResponseBodyConfigurationGrayVersions] = None,
        group: str = None,
        md_5: str = None,
        tags: str = None,
        type: str = None,
    ):
        # Application name.
        self.app_name = app_name
        # List of IPs for Beta release.
        self.beta_ips = beta_ips
        # Configuration content.
        self.content = content
        # Configuration ID.
        self.data_id = data_id
        # Configuration description.
        self.desc = desc
        # Encrypted key.
        self.encrypted_data_key = encrypted_data_key
        # Current gray version information
        self.gray_versions = gray_versions
        # Configuration group name.
        self.group = group
        # Message digest of the configuration.
        self.md_5 = md_5
        # Tags of the configuration.
        self.tags = tags
        # Format of the configuration content.
        self.type = type

    def validate(self):
        if self.gray_versions:
            for v1 in self.gray_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips

        if self.content is not None:
            result['Content'] = self.content

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key

        result['GrayVersions'] = []
        if self.gray_versions is not None:
            for k1 in self.gray_versions:
                result['GrayVersions'].append(k1.to_map() if k1 else None)

        if self.group is not None:
            result['Group'] = self.group

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')

        self.gray_versions = []
        if m.get('GrayVersions') is not None:
            for k1 in m.get('GrayVersions'):
                temp_model = main_models.GetNacosConfigResponseBodyConfigurationGrayVersions()
                self.gray_versions.append(temp_model.from_map(k1))

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetNacosConfigResponseBodyConfigurationGrayVersions(DaraModel):
    def __init__(
        self,
        name: str = None,
        priority: int = None,
        rule: str = None,
        type: str = None,
    ):
        # Gray version name
        self.name = name
        # The priority of the current gray rule.
        self.priority = priority
        # Rules of the current gray version
        self.rule = rule
        # Gray type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

