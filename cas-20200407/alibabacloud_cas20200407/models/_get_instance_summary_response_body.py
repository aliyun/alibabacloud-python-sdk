# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceSummaryResponseBody(DaraModel):
    def __init__(
        self,
        auto_reissue_count: int = None,
        certificate_count: int = None,
        inactive_count: int = None,
        request_id: str = None,
        total_count: int = None,
        will_expire_count: int = None,
    ):
        self.auto_reissue_count = auto_reissue_count
        self.certificate_count = certificate_count
        self.inactive_count = inactive_count
        self.request_id = request_id
        self.total_count = total_count
        self.will_expire_count = will_expire_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_reissue_count is not None:
            result['AutoReissueCount'] = self.auto_reissue_count

        if self.certificate_count is not None:
            result['CertificateCount'] = self.certificate_count

        if self.inactive_count is not None:
            result['InactiveCount'] = self.inactive_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.will_expire_count is not None:
            result['WillExpireCount'] = self.will_expire_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReissueCount') is not None:
            self.auto_reissue_count = m.get('AutoReissueCount')

        if m.get('CertificateCount') is not None:
            self.certificate_count = m.get('CertificateCount')

        if m.get('InactiveCount') is not None:
            self.inactive_count = m.get('InactiveCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('WillExpireCount') is not None:
            self.will_expire_count = m.get('WillExpireCount')

        return self

