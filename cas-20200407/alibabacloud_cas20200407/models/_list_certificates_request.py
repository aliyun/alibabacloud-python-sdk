# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCertificatesRequest(DaraModel):
    def __init__(
        self,
        certificate_source: str = None,
        certificate_status: str = None,
        current_page: int = None,
        instance_id: str = None,
        keyword: str = None,
        resource_group_id: str = None,
        show_size: int = None,
    ):
        self.certificate_source = certificate_source
        self.certificate_status = certificate_status
        self.current_page = current_page
        self.instance_id = instance_id
        self.keyword = keyword
        self.resource_group_id = resource_group_id
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_source is not None:
            result['CertificateSource'] = self.certificate_source

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateSource') is not None:
            self.certificate_source = m.get('CertificateSource')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

