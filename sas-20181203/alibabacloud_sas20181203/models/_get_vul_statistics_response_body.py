# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVulStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vul_asap_sum: int = None,
        vul_later_sum: int = None,
        vul_nntf_sum: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of vulnerabilities that have the high priority.
        self.vul_asap_sum = vul_asap_sum
        # The number of vulnerabilities that have the medium priority.
        self.vul_later_sum = vul_later_sum
        # The number of vulnerabilities that have the low priority.
        self.vul_nntf_sum = vul_nntf_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vul_asap_sum is not None:
            result['VulAsapSum'] = self.vul_asap_sum

        if self.vul_later_sum is not None:
            result['VulLaterSum'] = self.vul_later_sum

        if self.vul_nntf_sum is not None:
            result['VulNntfSum'] = self.vul_nntf_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VulAsapSum') is not None:
            self.vul_asap_sum = m.get('VulAsapSum')

        if m.get('VulLaterSum') is not None:
            self.vul_later_sum = m.get('VulLaterSum')

        if m.get('VulNntfSum') is not None:
            self.vul_nntf_sum = m.get('VulNntfSum')

        return self

