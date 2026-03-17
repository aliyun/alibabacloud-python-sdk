# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeACLAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acrs: main_models.DescribeACLAttributeResponseBodyAcrs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.acrs = acrs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.acrs:
            self.acrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acrs is not None:
            result['Acrs'] = self.acrs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acrs') is not None:
            temp_model = main_models.DescribeACLAttributeResponseBodyAcrs()
            self.acrs = temp_model.from_map(m.get('Acrs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeACLAttributeResponseBodyAcrs(DaraModel):
    def __init__(
        self,
        acr: List[main_models.DescribeACLAttributeResponseBodyAcrsAcr] = None,
    ):
        self.acr = acr

    def validate(self):
        if self.acr:
            for v1 in self.acr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Acr'] = []
        if self.acr is not None:
            for k1 in self.acr:
                result['Acr'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr = []
        if m.get('Acr') is not None:
            for k1 in m.get('Acr'):
                temp_model = main_models.DescribeACLAttributeResponseBodyAcrsAcr()
                self.acr.append(temp_model.from_map(k1))

        return self

class DescribeACLAttributeResponseBodyAcrsAcr(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_type: str = None,
        acr_id: str = None,
        description: str = None,
        dest_cidr: str = None,
        dest_port_range: str = None,
        direction: str = None,
        dpi_group_ids: main_models.DescribeACLAttributeResponseBodyAcrsAcrDpiGroupIds = None,
        dpi_signature_ids: main_models.DescribeACLAttributeResponseBodyAcrsAcrDpiSignatureIds = None,
        gmt_create: int = None,
        ip_protocol: str = None,
        name: str = None,
        policy: str = None,
        priority: int = None,
        source_cidr: str = None,
        source_port_range: str = None,
        type: str = None,
    ):
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acr_id = acr_id
        self.description = description
        self.dest_cidr = dest_cidr
        self.dest_port_range = dest_port_range
        self.direction = direction
        self.dpi_group_ids = dpi_group_ids
        self.dpi_signature_ids = dpi_signature_ids
        self.gmt_create = gmt_create
        self.ip_protocol = ip_protocol
        self.name = name
        self.policy = policy
        self.priority = priority
        self.source_cidr = source_cidr
        self.source_port_range = source_port_range
        self.type = type

    def validate(self):
        if self.dpi_group_ids:
            self.dpi_group_ids.validate()
        if self.dpi_signature_ids:
            self.dpi_signature_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.acr_id is not None:
            result['AcrId'] = self.acr_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_cidr is not None:
            result['DestCidr'] = self.dest_cidr

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dpi_group_ids is not None:
            result['DpiGroupIds'] = self.dpi_group_ids.to_map()

        if self.dpi_signature_ids is not None:
            result['DpiSignatureIds'] = self.dpi_signature_ids.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('AcrId') is not None:
            self.acr_id = m.get('AcrId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestCidr') is not None:
            self.dest_cidr = m.get('DestCidr')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DpiGroupIds') is not None:
            temp_model = main_models.DescribeACLAttributeResponseBodyAcrsAcrDpiGroupIds()
            self.dpi_group_ids = temp_model.from_map(m.get('DpiGroupIds'))

        if m.get('DpiSignatureIds') is not None:
            temp_model = main_models.DescribeACLAttributeResponseBodyAcrsAcrDpiSignatureIds()
            self.dpi_signature_ids = temp_model.from_map(m.get('DpiSignatureIds'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeACLAttributeResponseBodyAcrsAcrDpiSignatureIds(DaraModel):
    def __init__(
        self,
        dpi_signature_id: List[str] = None,
    ):
        self.dpi_signature_id = dpi_signature_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_signature_id is not None:
            result['DpiSignatureId'] = self.dpi_signature_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiSignatureId') is not None:
            self.dpi_signature_id = m.get('DpiSignatureId')

        return self

class DescribeACLAttributeResponseBodyAcrsAcrDpiGroupIds(DaraModel):
    def __init__(
        self,
        dpi_group_id: List[str] = None,
    ):
        self.dpi_group_id = dpi_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_group_id is not None:
            result['DpiGroupId'] = self.dpi_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiGroupId') is not None:
            self.dpi_group_id = m.get('DpiGroupId')

        return self

