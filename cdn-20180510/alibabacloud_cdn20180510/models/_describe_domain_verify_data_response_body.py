# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainVerifyDataResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeDomainVerifyDataResponseBodyContent = None,
        request_id: str = None,
    ):
        # The verification content.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeDomainVerifyDataResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainVerifyDataResponseBodyContent(DaraModel):
    def __init__(
        self,
        root_domain: str = None,
        verify_code: str = None,
        verify_key: str = None,
    ):
        self.root_domain = root_domain
        self.verify_code = verify_code
        self.verify_key = verify_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain

        if self.verify_code is not None:
            result['verifyCode'] = self.verify_code

        if self.verify_key is not None:
            result['verifyKey'] = self.verify_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')

        if m.get('verifyCode') is not None:
            self.verify_code = m.get('verifyCode')

        if m.get('verifyKey') is not None:
            self.verify_key = m.get('verifyKey')

        return self

