# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        brand: str = None,
        certificate_status: str = None,
        certificate_type: str = None,
        current_page: int = None,
        instance_type: str = None,
        keyword: str = None,
        resource_group_id: str = None,
        show_size: int = None,
        status: str = None,
    ):
        self.brand = brand
        self.certificate_status = certificate_status
        self.certificate_type = certificate_type
        self.current_page = current_page
        self.instance_type = instance_type
        self.keyword = keyword
        self.resource_group_id = resource_group_id
        self.show_size = show_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand is not None:
            result['Brand'] = self.brand

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

