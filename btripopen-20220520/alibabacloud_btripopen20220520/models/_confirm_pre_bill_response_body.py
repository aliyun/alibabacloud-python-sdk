# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ConfirmPreBillResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.ConfirmPreBillResponseBodyModule = None,
        more_page: bool = None,
        request_id: str = None,
        result_code: int = None,
        result_msg: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The details of the returned result.
        self.module = module
        # The pagination token set by the server. Indicates whether more data is available on the next page during pagination.
        self.more_page = more_page
        # The unique identifier of the request.
        self.request_id = request_id
        # The error code.
        self.result_code = result_code
        # The error message.
        self.result_msg = result_msg
        # Indicates whether the API call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed.
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.more_page is not None:
            result['more_page'] = self.more_page

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_code is not None:
            result['result_code'] = self.result_code

        if self.result_msg is not None:
            result['result_msg'] = self.result_msg

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = main_models.ConfirmPreBillResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')

        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class ConfirmPreBillResponseBodyModule(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        forbid_update_bill_count: int = None,
        forbid_update_detail: List[main_models.ConfirmPreBillResponseBodyModuleForbidUpdateDetail] = None,
        match_count: int = None,
        not_match_count: int = None,
        not_match_detail: List[str] = None,
    ):
        # The batch ID.
        self.batch_id = batch_id
        # The number of bills that cannot be updated.
        self.forbid_update_bill_count = forbid_update_bill_count
        # The details of items that cannot be updated.
        self.forbid_update_detail = forbid_update_detail
        # The number of matched items.
        self.match_count = match_count
        # The number of unmatched items.
        self.not_match_count = not_match_count
        # The details of unmatched items.
        self.not_match_detail = not_match_detail

    def validate(self):
        if self.forbid_update_detail:
            for v1 in self.forbid_update_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batch_id'] = self.batch_id

        if self.forbid_update_bill_count is not None:
            result['forbid_update_bill_count'] = self.forbid_update_bill_count

        result['forbid_update_detail'] = []
        if self.forbid_update_detail is not None:
            for k1 in self.forbid_update_detail:
                result['forbid_update_detail'].append(k1.to_map() if k1 else None)

        if self.match_count is not None:
            result['match_count'] = self.match_count

        if self.not_match_count is not None:
            result['not_match_count'] = self.not_match_count

        if self.not_match_detail is not None:
            result['not_match_detail'] = self.not_match_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batch_id') is not None:
            self.batch_id = m.get('batch_id')

        if m.get('forbid_update_bill_count') is not None:
            self.forbid_update_bill_count = m.get('forbid_update_bill_count')

        self.forbid_update_detail = []
        if m.get('forbid_update_detail') is not None:
            for k1 in m.get('forbid_update_detail'):
                temp_model = main_models.ConfirmPreBillResponseBodyModuleForbidUpdateDetail()
                self.forbid_update_detail.append(temp_model.from_map(k1))

        if m.get('match_count') is not None:
            self.match_count = m.get('match_count')

        if m.get('not_match_count') is not None:
            self.not_match_count = m.get('not_match_count')

        if m.get('not_match_detail') is not None:
            self.not_match_detail = m.get('not_match_detail')

        return self

class ConfirmPreBillResponseBodyModuleForbidUpdateDetail(DaraModel):
    def __init__(
        self,
        can_not_update_count: int = None,
        can_update_count: int = None,
        value: str = None,
    ):
        # The number of items that cannot be updated.
        self.can_not_update_count = can_not_update_count
        # The number of items that can be updated.
        self.can_update_count = can_update_count
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_not_update_count is not None:
            result['can_not_update_count'] = self.can_not_update_count

        if self.can_update_count is not None:
            result['can_update_count'] = self.can_update_count

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_not_update_count') is not None:
            self.can_not_update_count = m.get('can_not_update_count')

        if m.get('can_update_count') is not None:
            self.can_update_count = m.get('can_update_count')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

