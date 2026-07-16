# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUuidsByVulNamesRequest(DaraModel):
    def __init__(
        self,
        dealed: str = None,
        field_name: str = None,
        field_value: str = None,
        group_id: int = None,
        lang: str = None,
        level: str = None,
        necessity: str = None,
        remark: str = None,
        search_tags: str = None,
        status_list: str = None,
        tag: str = None,
        target_type: str = None,
        type: str = None,
        vpc_instance_ids: str = None,
        vul_names: List[str] = None,
    ):
        # Specifies whether the vulnerability has been handled. Valid values:
        # - **y**: handled
        # - **n**: not handled.
        self.dealed = dealed
        # The container search field name.
        self.field_name = field_name
        # The container search field value.
        self.field_value = field_value
        # The ID of the asset group.
        self.group_id = group_id
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The vulnerability level. Separate multiple levels with commas (,). Valid values:
        # 
        # - **high**: high
        # - **medium**: medium
        # - **low**: low.
        self.level = level
        # The priority level of vulnerability fixing. Separate multiple levels with commas (,). Valid values:
        # 
        # - **asap**: high
        # - **later**: medium
        # - **nntf**: low.
        self.necessity = necessity
        # The asset information for the vulnerability query. You can set this parameter to the asset name, public IP address, or private IP address. Fuzzy match is supported.
        self.remark = remark
        # The tag for querying vulnerabilities.
        self.search_tags = search_tags
        # The fix status of the vulnerability. Separate multiple statuses with commas (,). Valid values:
        # 
        # - **1**: unfixed
        # - **2**: fix failed.
        self.status_list = status_list
        # The vulnerability tag.
        self.tag = tag
        # The query type. Valid values:
        # 
        # - **containerId**: container ID
        # - **uuid**: asset ID.
        self.target_type = target_type
        # The type of vulnerability to query. Valid values:
        # 
        # - **cve**: Linux software vulnerability
        # - **sys**: Windows system vulnerability.
        # 
        # This parameter is required.
        self.type = type
        # The instance IDs of VPC-connected instances to query for vulnerabilities. Separate multiple instance IDs with commas (,).
        self.vpc_instance_ids = vpc_instance_ids
        # The collection of vulnerability names.
        # > You can call the [DescribeGroupedVul](~~DescribeGroupedVul~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.vul_names = vul_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.search_tags is not None:
            result['SearchTags'] = self.search_tags

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        if self.vpc_instance_ids is not None:
            result['VpcInstanceIds'] = self.vpc_instance_ids

        if self.vul_names is not None:
            result['VulNames'] = self.vul_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SearchTags') is not None:
            self.search_tags = m.get('SearchTags')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpcInstanceIds') is not None:
            self.vpc_instance_ids = m.get('VpcInstanceIds')

        if m.get('VulNames') is not None:
            self.vul_names = m.get('VulNames')

        return self

