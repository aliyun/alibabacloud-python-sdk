# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcVersion(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        company_name: str = None,
        developer_id: int = None,
        id: int = None,
        is_watched: bool = None,
        name: str = None,
        pbc_id: int = None,
        request_id: str = None,
        review_id: int = None,
        status: str = None,
        step_status: str = None,
        version: str = None,
        visibility_level: str = None,
    ):
        self.company_id = company_id
        self.company_name = company_name
        self.developer_id = developer_id
        self.id = id
        self.is_watched = is_watched
        # This parameter is required.
        self.name = name
        self.pbc_id = pbc_id
        self.request_id = request_id
        self.review_id = review_id
        self.status = status
        # This parameter is required.
        self.step_status = step_status
        # This parameter is required.
        self.version = version
        # This parameter is required.
        self.visibility_level = visibility_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.company_name is not None:
            result['companyName'] = self.company_name

        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.id is not None:
            result['id'] = self.id

        if self.is_watched is not None:
            result['isWatched'] = self.is_watched

        if self.name is not None:
            result['name'] = self.name

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.review_id is not None:
            result['reviewId'] = self.review_id

        if self.status is not None:
            result['status'] = self.status

        if self.step_status is not None:
            result['stepStatus'] = self.step_status

        if self.version is not None:
            result['version'] = self.version

        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('companyName') is not None:
            self.company_name = m.get('companyName')

        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isWatched') is not None:
            self.is_watched = m.get('isWatched')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewId') is not None:
            self.review_id = m.get('reviewId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stepStatus') is not None:
            self.step_status = m.get('stepStatus')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')

        return self

