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
        search_tags: str = None,
        type: str = None,
        uuids: str = None,
        vpc_instance_ids: str = None,
        vul_entity_list: List[main_models.ExportVulRequestVulEntityList] = None,
    ):
        # The name of the vulnerability.
        self.alias_name = alias_name
        # The additional type of the vulnerabilities. You need to specify this parameter when you query application vulnerabilities. If you set the Type parameter to app, you must specify this parameter. Set the value to **sca**.
        # 
        # > If this parameter is set to **sca**, **application vulnerabilities** and the **vulnerabilities that are detected based on software component analysis** are queried. If you do not specify this parameter, only application vulnerabilities are queried.
        self.attach_types = attach_types
        # The name of the container that is affected by the vulnerability.
        self.container_name = container_name
        # The end time of the first scan.
        # 
        # >  This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_ts_end = create_ts_end
        # The start time of the first scan.
        # 
        # >  This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_ts_start = create_ts_start
        # The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability.
        self.cve_id = cve_id
        # Specifies whether the vulnerability is fixed. Valid values:
        # 
        # *   **y**: The vulnerability is fixed.
        # *   **n**: The vulnerability is not fixed.
        self.dealed = dealed
        # The server group ID of the server on which the vulnerabilities are detected.
        # 
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of server groups.
        self.group_id = group_id
        # The name of the image that is affected by the vulnerability.
        self.image_name = image_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.lang = lang
        # The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values:
        # 
        # *   **asap**: high
        # *   **later**: medium
        # *   **nntf**: low
        self.necessity = necessity
        # The path of the process that is affected by the vulnerability.
        self.path = path
        # Indicates whether the application protection feature is supported. Valid values:
        # 
        # - **0**: no.
        # 
        # - **1**: yes.
        self.rasp_defend = rasp_defend
        # The tag that is used to search for the vulnerabilities. Valid values:
        # 
        # *   Restart required
        # *   Remote exploitation
        # *   Exploit exists
        # *   Exploitable
        # *   Privilege escalation
        # *   Code execution
        self.search_tags = search_tags
        # The type of the vulnerability that you want to export. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **app**: application vulnerability
        # *   **emg**: urgent vulnerability
        # 
        # This parameter is required.
        self.type = type
        # The UUID of the server on which the vulnerabilities are detected. Separate multiple UUIDs with commas (,).
        self.uuids = uuids
        # The ID of the virtual private cloud (VPC) in which the vulnerabilities are detected. Separate multiple IDs with commas (,).
        # 
        # > You can call the [DescribeVpcList](~~DescribeVpcList~~) operation to query the IDs of VPCs.
        self.vpc_instance_ids = vpc_instance_ids
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
        self.entity_name = entity_name
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

