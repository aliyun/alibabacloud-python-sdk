# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class UpdateTagOptionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tag_option_detail: main_models.UpdateTagOptionResponseBodyTagOptionDetail = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the tag option.
        self.tag_option_detail = tag_option_detail

    def validate(self):
        if self.tag_option_detail:
            self.tag_option_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_option_detail is not None:
            result['TagOptionDetail'] = self.tag_option_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagOptionDetail') is not None:
            temp_model = main_models.UpdateTagOptionResponseBodyTagOptionDetail()
            self.tag_option_detail = temp_model.from_map(m.get('TagOptionDetail'))

        return self

class UpdateTagOptionResponseBodyTagOptionDetail(DaraModel):
    def __init__(
        self,
        active: bool = None,
        key: str = None,
        owner: str = None,
        tag_option_id: str = None,
        value: str = None,
    ):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active
        # The key of the tag option.
        # 
        # The key must be 1 to 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.key = key
        # The ID of the Alibaba Cloud account to which the tag option belongs.
        self.owner = owner
        # The ID of the tag option.
        self.tag_option_id = tag_option_id
        # The value of the tag option.
        # 
        # The value must be 1 to 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.key is not None:
            result['Key'] = self.key

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

