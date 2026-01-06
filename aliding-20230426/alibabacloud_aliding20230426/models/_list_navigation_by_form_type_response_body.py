# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListNavigationByFormTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListNavigationByFormTypeResponseBodyResult] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListNavigationByFormTypeResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListNavigationByFormTypeResponseBodyResult(DaraModel):
    def __init__(
        self,
        form_uuid: str = None,
        process_code: str = None,
        title: main_models.ListNavigationByFormTypeResponseBodyResultTitle = None,
    ):
        self.form_uuid = form_uuid
        self.process_code = process_code
        self.title = title

    def validate(self):
        if self.title:
            self.title.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.process_code is not None:
            result['ProcessCode'] = self.process_code

        if self.title is not None:
            result['Title'] = self.title.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('ProcessCode') is not None:
            self.process_code = m.get('ProcessCode')

        if m.get('Title') is not None:
            temp_model = main_models.ListNavigationByFormTypeResponseBodyResultTitle()
            self.title = temp_model.from_map(m.get('Title'))

        return self

class ListNavigationByFormTypeResponseBodyResultTitle(DaraModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        self.name_in_chinese = name_in_chinese
        self.name_in_english = name_in_english
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_in_chinese is not None:
            result['NameInChinese'] = self.name_in_chinese

        if self.name_in_english is not None:
            result['NameInEnglish'] = self.name_in_english

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameInChinese') is not None:
            self.name_in_chinese = m.get('NameInChinese')

        if m.get('NameInEnglish') is not None:
            self.name_in_english = m.get('NameInEnglish')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

