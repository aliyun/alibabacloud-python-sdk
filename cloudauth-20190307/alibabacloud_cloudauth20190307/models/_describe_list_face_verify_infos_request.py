# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeListFaceVerifyInfosRequest(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        gmt_end: int = None,
        gmt_start: int = None,
        page_number: int = None,
        page_size: int = None,
        scene_id: int = None,
        status: int = None,
    ):
        # Verification ID.
        self.certify_id = certify_id
        # Query the end time of the verification.
        self.gmt_end = gmt_end
        # Query the start time of the verification.
        self.gmt_start = gmt_start
        # Pagination parameter: current page number.
        self.page_number = page_number
        # Number of items per page for paginated queries. Maximum value: 100, default value: 10.
        self.page_size = page_size
        # Scene ID.
        self.scene_id = scene_id
        # Verification status:
        # - **1**: Verification passed.
        # - **2**: Verification failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.gmt_end is not None:
            result['GmtEnd'] = self.gmt_end

        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('GmtEnd') is not None:
            self.gmt_end = m.get('GmtEnd')

        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

