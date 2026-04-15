# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class SaveOrderRelationInfoToMsenceResponseBody(DaraModel):
    def __init__(
        self,
        mpaas_save_order_relation_response: main_models.SaveOrderRelationInfoToMsenceResponseBodyMpaasSaveOrderRelationResponse = None,
        request_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mpaas_save_order_relation_response = mpaas_save_order_relation_response
        # Id of the request
        self.request_id = request_id
        self.result_code = result_code
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mpaas_save_order_relation_response:
            self.mpaas_save_order_relation_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpaas_save_order_relation_response is not None:
            result['MpaasSaveOrderRelationResponse'] = self.mpaas_save_order_relation_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MpaasSaveOrderRelationResponse') is not None:
            temp_model = main_models.SaveOrderRelationInfoToMsenceResponseBodyMpaasSaveOrderRelationResponse()
            self.mpaas_save_order_relation_response = temp_model.from_map(m.get('MpaasSaveOrderRelationResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SaveOrderRelationInfoToMsenceResponseBodyMpaasSaveOrderRelationResponse(DaraModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

