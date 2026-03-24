# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnTypesResponseBody(DaraModel):
    def __init__(
        self,
        cdn_types: main_models.DescribeCdnTypesResponseBodyCdnTypes = None,
        request_id: str = None,
    ):
        self.cdn_types = cdn_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cdn_types:
            self.cdn_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_types is not None:
            result['CdnTypes'] = self.cdn_types.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnTypes') is not None:
            temp_model = main_models.DescribeCdnTypesResponseBodyCdnTypes()
            self.cdn_types = temp_model.from_map(m.get('CdnTypes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnTypesResponseBodyCdnTypes(DaraModel):
    def __init__(
        self,
        cdn_type: List[main_models.DescribeCdnTypesResponseBodyCdnTypesCdnType] = None,
    ):
        self.cdn_type = cdn_type

    def validate(self):
        if self.cdn_type:
            for v1 in self.cdn_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CdnType'] = []
        if self.cdn_type is not None:
            for k1 in self.cdn_type:
                result['CdnType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cdn_type = []
        if m.get('CdnType') is not None:
            for k1 in m.get('CdnType'):
                temp_model = main_models.DescribeCdnTypesResponseBodyCdnTypesCdnType()
                self.cdn_type.append(temp_model.from_map(k1))

        return self

class DescribeCdnTypesResponseBodyCdnTypesCdnType(DaraModel):
    def __init__(
        self,
        desc: str = None,
        type: str = None,
    ):
        self.desc = desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

