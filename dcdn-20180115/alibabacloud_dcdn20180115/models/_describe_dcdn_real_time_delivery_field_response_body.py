# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnRealTimeDeliveryFieldResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeDcdnRealTimeDeliveryFieldResponseBodyContent = None,
        request_id: str = None,
    ):
        # The returned results.
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
            temp_model = main_models.DescribeDcdnRealTimeDeliveryFieldResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnRealTimeDeliveryFieldResponseBodyContent(DaraModel):
    def __init__(
        self,
        fields: List[main_models.DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields] = None,
    ):
        self.fields = fields

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields()
                self.fields.append(temp_model.from_map(k1))

        return self

class DescribeDcdnRealTimeDeliveryFieldResponseBodyContentFields(DaraModel):
    def __init__(
        self,
        description: str = None,
        field_name: str = None,
    ):
        # The description of the field.
        self.description = description
        # The name of the field. For more information about fields in real-time log entries, see [Fields in a real-time log](https://help.aliyun.com/document_detail/324199.html).
        self.field_name = field_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        return self

