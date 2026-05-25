# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class GetErrorsResponseBody(DaraModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: main_models.GetErrorsResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        # RequestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.GetErrorsResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetErrorsResponseBodyModel(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetErrorsResponseBodyModelItems] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.pages = pages
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pages is not None:
            result['Pages'] = self.pages

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetErrorsResponseBodyModelItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pages') is not None:
            self.pages = m.get('Pages')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetErrorsResponseBodyModelItems(DaraModel):
    def __init__(
        self,
        client_time: int = None,
        did: str = None,
        digest_hash: str = None,
        utdid: str = None,
        uuid: str = None,
    ):
        self.client_time = client_time
        self.did = did
        self.digest_hash = digest_hash
        # Utdid
        self.utdid = utdid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_time is not None:
            result['ClientTime'] = self.client_time

        if self.did is not None:
            result['Did'] = self.did

        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash

        if self.utdid is not None:
            result['Utdid'] = self.utdid

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientTime') is not None:
            self.client_time = m.get('ClientTime')

        if m.get('Did') is not None:
            self.did = m.get('Did')

        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')

        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

