# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ExportVulRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        asset_type: str = None,
        attach_types: str = None,
        container_name: str = None,
        create_ts_end: int = None,
        create_ts_start: int = None,
        cve_id: str = None,
        dealed: str = None,
        group_id: str = None,
        image_name: str = None,
        lang: str = None,
        necessity: str = None,
        path: str = None,
        rasp_defend: int = None,
        resource_directory_account_id: int = None,
        search_tags: str = None,
        type: str = None,
        uuids: str = None,
        vpc_instance_ids: str = None,
        vul_entity_list: List[main_models.ExportVulRequestVulEntityList] = None,
    ):
        # The name of the vulnerability.
        self.alias_name = alias_name
        # The asset type where the vulnerability resides. Separate multiple types with commas (,). Valid values:
        # - **ECS**: server asset
        # - **CONTAINER**: container asset
        self.asset_type = asset_type
        # The additional vulnerability type when you query application vulnerabilities. You must configure this parameter when you query application vulnerabilities, which means the Type parameter is set to app. Set the value to **sca**.
        # 
        # > If you set this parameter to **sca**, you can query application vulnerabilities (type **app**) and software composition analysis (type **sca**) vulnerabilities. If you do not set this parameter, only application vulnerabilities are queried.
        self.attach_types = attach_types
        # The name of the container affected by the vulnerabilities to be queried.
        self.container_name = container_name
        # The end time of the first scan.
        # > The value is a UNIX timestamp. Unit: milliseconds.
        self.create_ts_end = create_ts_end
        # The start time of the first scan.
        # > The value is a UNIX timestamp. Unit: milliseconds.
        self.create_ts_start = create_ts_start
        # The CVE ID.
        self.cve_id = cve_id
        # Specifies whether the vulnerabilities to be queried are fixed. Valid values:
        # 
        # - **y**: fixed
        # - **n**: unfixed
        self.dealed = dealed
        # The ID of the asset group to which the servers affected by the vulnerabilities to be queried belong.
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to obtain the value of this parameter.
        self.group_id = group_id
        # The name of the image affected by the vulnerabilities to be queried.
        self.image_name = image_name
        # Specifies the language of the request and response. Default value: **zh**. Valid values:
        # 
        # - zh: Chinese
        # - en: English
        self.lang = lang
        # The priorities of the vulnerabilities to be queried. Separate multiple priorities with commas (,). Valid values:
        # 
        # - **asap**: high
        # - **later**: medium
        # - **nntf**: low
        self.necessity = necessity
        # The path of the process affected by the vulnerabilities to be queried.
        self.path = path
        # Specifies whether Runtime Application Self-Protection (RASP) supports real-time protection against the vulnerability. Valid values:
        # 
        # - **0**: not supported
        # - **1**: supported
        self.rasp_defend = rasp_defend
        # The ID of the resource directory account.
        self.resource_directory_account_id = resource_directory_account_id
        # The tags used for filtering. Valid values:
        # 
        # <props="china">
        # - Restart required
        # - Remote exploitation
        # - EXP exists
        # - Exploitable
        # - Privilege escalation
        # - Code execution
        # 
        # 
        # <props="intl">
        # - **Restart required**
        # - **Remote utilization**
        # - **EXP exists**
        # - **Available**
        # - **Elevation of privilege**
        # - **Code execution**
        self.search_tags = search_tags
        # The type of the vulnerabilities to be exported. Valid values:
        # 
        # - **cve**: Linux software vulnerability
        # - **sys**: Windows system vulnerability
        # - **cms**: Web-CMS vulnerability
        # - **app**: application vulnerability
        # - **emg**: emergency vulnerability
        # 
        # This parameter is required.
        self.type = type
        # The UUIDs of the servers on which you want to query vulnerabilities. Separate multiple UUIDs with commas (,).
        self.uuids = uuids
        # The IDs of the VPC-connected instances where the vulnerabilities to be queried reside. Separate multiple IDs with commas (,).
        # > You can call the [DescribeVpcList](~~DescribeVpcList~~) operation to obtain the value of this parameter.
        self.vpc_instance_ids = vpc_instance_ids
        # The list of vulnerability component information.
        self.vul_entity_list = vul_entity_list

    def validate(self):
        if self.vul_entity_list:
            for v1 in self.vul_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.attach_types is not None:
            result['AttachTypes'] = self.attach_types

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.create_ts_end is not None:
            result['CreateTsEnd'] = self.create_ts_end

        if self.create_ts_start is not None:
            result['CreateTsStart'] = self.create_ts_start

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.path is not None:
            result['Path'] = self.path

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.search_tags is not None:
            result['SearchTags'] = self.search_tags

        if self.type is not None:
            result['Type'] = self.type

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.vpc_instance_ids is not None:
            result['VpcInstanceIds'] = self.vpc_instance_ids

        result['VulEntityList'] = []
        if self.vul_entity_list is not None:
            for k1 in self.vul_entity_list:
                result['VulEntityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AttachTypes') is not None:
            self.attach_types = m.get('AttachTypes')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('CreateTsEnd') is not None:
            self.create_ts_end = m.get('CreateTsEnd')

        if m.get('CreateTsStart') is not None:
            self.create_ts_start = m.get('CreateTsStart')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SearchTags') is not None:
            self.search_tags = m.get('SearchTags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('VpcInstanceIds') is not None:
            self.vpc_instance_ids = m.get('VpcInstanceIds')

        self.vul_entity_list = []
        if m.get('VulEntityList') is not None:
            for k1 in m.get('VulEntityList'):
                temp_model = main_models.ExportVulRequestVulEntityList()
                self.vul_entity_list.append(temp_model.from_map(k1))

        return self

class ExportVulRequestVulEntityList(DaraModel):
    def __init__(
        self,
        entity_name: str = None,
        entity_version: str = None,
    ):
        # The name of the component.
        self.entity_name = entity_name
        # The version of the component.
        self.entity_version = entity_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_version is not None:
            result['EntityVersion'] = self.entity_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityVersion') is not None:
            self.entity_version = m.get('EntityVersion')

        return self

