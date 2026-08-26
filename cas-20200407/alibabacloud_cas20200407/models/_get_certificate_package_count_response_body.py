# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCertificatePackageCountResponseBody(DaraModel):
    def __init__(
        self,
        notice_count_detail: str = None,
        product_count_list: str = None,
        proxy_count_detail: str = None,
        request_id: str = None,
        total_count_detail: str = None,
        trustee_count_detail: str = None,
    ):
        # The message notification quota.
        self.notice_count_detail = notice_count_detail
        # The details of certificate brand products.
        self.product_count_list = product_count_list
        # The acceleration gateway forwarding quota.
        self.proxy_count_detail = proxy_count_detail
        # The request ID.
        self.request_id = request_id
        # The total number of domain names bound to certificates.
        self.total_count_detail = total_count_detail
        # The usage of the hosting quota.
        self.trustee_count_detail = trustee_count_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notice_count_detail is not None:
            result['NoticeCountDetail'] = self.notice_count_detail

        if self.product_count_list is not None:
            result['ProductCountList'] = self.product_count_list

        if self.proxy_count_detail is not None:
            result['ProxyCountDetail'] = self.proxy_count_detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count_detail is not None:
            result['TotalCountDetail'] = self.total_count_detail

        if self.trustee_count_detail is not None:
            result['TrusteeCountDetail'] = self.trustee_count_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoticeCountDetail') is not None:
            self.notice_count_detail = m.get('NoticeCountDetail')

        if m.get('ProductCountList') is not None:
            self.product_count_list = m.get('ProductCountList')

        if m.get('ProxyCountDetail') is not None:
            self.proxy_count_detail = m.get('ProxyCountDetail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCountDetail') is not None:
            self.total_count_detail = m.get('TotalCountDetail')

        if m.get('TrusteeCountDetail') is not None:
            self.trustee_count_detail = m.get('TrusteeCountDetail')

        return self

