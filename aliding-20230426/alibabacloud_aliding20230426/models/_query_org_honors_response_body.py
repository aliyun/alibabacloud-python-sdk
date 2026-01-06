# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryOrgHonorsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        open_honors: List[main_models.QueryOrgHonorsResponseBodyOpenHonors] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.open_honors = open_honors
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.open_honors:
            for v1 in self.open_honors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['openHonors'] = []
        if self.open_honors is not None:
            for k1 in self.open_honors:
                result['openHonors'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.open_honors = []
        if m.get('openHonors') is not None:
            for k1 in m.get('openHonors'):
                temp_model = main_models.QueryOrgHonorsResponseBodyOpenHonors()
                self.open_honors.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryOrgHonorsResponseBodyOpenHonors(DaraModel):
    def __init__(
        self,
        honor_desc: str = None,
        honor_id: int = None,
        honor_img_url: str = None,
        honor_name: str = None,
        honor_pendant_img_url: str = None,
    ):
        self.honor_desc = honor_desc
        self.honor_id = honor_id
        self.honor_img_url = honor_img_url
        self.honor_name = honor_name
        self.honor_pendant_img_url = honor_pendant_img_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honor_desc is not None:
            result['honorDesc'] = self.honor_desc

        if self.honor_id is not None:
            result['honorId'] = self.honor_id

        if self.honor_img_url is not None:
            result['honorImgUrl'] = self.honor_img_url

        if self.honor_name is not None:
            result['honorName'] = self.honor_name

        if self.honor_pendant_img_url is not None:
            result['honorPendantImgUrl'] = self.honor_pendant_img_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('honorDesc') is not None:
            self.honor_desc = m.get('honorDesc')

        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')

        if m.get('honorImgUrl') is not None:
            self.honor_img_url = m.get('honorImgUrl')

        if m.get('honorName') is not None:
            self.honor_name = m.get('honorName')

        if m.get('honorPendantImgUrl') is not None:
            self.honor_pendant_img_url = m.get('honorPendantImgUrl')

        return self

