# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetConversaionSpaceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        space: main_models.GetConversaionSpaceResponseBodySpace = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.space = space
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.space:
            self.space.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.space is not None:
            result['space'] = self.space.to_map()

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('space') is not None:
            temp_model = main_models.GetConversaionSpaceResponseBodySpace()
            self.space = temp_model.from_map(m.get('space'))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetConversaionSpaceResponseBodySpace(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        create_time: str = None,
        modified_time: str = None,
        space_id: str = None,
    ):
        self.corp_id = corp_id
        self.create_time = create_time
        self.modified_time = modified_time
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        return self

