# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetSaseUserTagResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sase_user_tag: main_models.GetSaseUserTagResponseBodySaseUserTag = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The user tag response body.
        self.sase_user_tag = sase_user_tag

    def validate(self):
        if self.sase_user_tag:
            self.sase_user_tag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sase_user_tag is not None:
            result['SaseUserTag'] = self.sase_user_tag.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SaseUserTag') is not None:
            temp_model = main_models.GetSaseUserTagResponseBodySaseUserTag()
            self.sase_user_tag = temp_model.from_map(m.get('SaseUserTag'))

        return self

class GetSaseUserTagResponseBodySaseUserTag(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.aliuid = aliuid
        # The user tag description.
        self.description = description
        # The user tag name.
        self.name = name
        # The user tag ID.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

