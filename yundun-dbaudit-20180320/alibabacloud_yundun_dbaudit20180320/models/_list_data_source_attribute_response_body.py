# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        db_list: List[main_models.ListDataSourceAttributeResponseBodyDbList] = None,
        request_id: str = None,
    ):
        self.db_list = db_list
        self.request_id = request_id

    def validate(self):
        if self.db_list:
            for v1 in self.db_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DbList'] = []
        if self.db_list is not None:
            for k1 in self.db_list:
                result['DbList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_list = []
        if m.get('DbList') is not None:
            for k1 in m.get('DbList'):
                temp_model = main_models.ListDataSourceAttributeResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourceAttributeResponseBodyDbList(DaraModel):
    def __init__(
        self,
        audit_mode: str = None,
        db_id: int = None,
        freq_audit_mode: str = None,
        result_audit_max_line: int = None,
        result_audit_max_size: int = None,
        result_audit_mode: str = None,
    ):
        self.audit_mode = audit_mode
        self.db_id = db_id
        self.freq_audit_mode = freq_audit_mode
        self.result_audit_max_line = result_audit_max_line
        self.result_audit_max_size = result_audit_max_size
        self.result_audit_mode = result_audit_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.freq_audit_mode is not None:
            result['FreqAuditMode'] = self.freq_audit_mode

        if self.result_audit_max_line is not None:
            result['ResultAuditMaxLine'] = self.result_audit_max_line

        if self.result_audit_max_size is not None:
            result['ResultAuditMaxSize'] = self.result_audit_max_size

        if self.result_audit_mode is not None:
            result['ResultAuditMode'] = self.result_audit_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('FreqAuditMode') is not None:
            self.freq_audit_mode = m.get('FreqAuditMode')

        if m.get('ResultAuditMaxLine') is not None:
            self.result_audit_max_line = m.get('ResultAuditMaxLine')

        if m.get('ResultAuditMaxSize') is not None:
            self.result_audit_max_size = m.get('ResultAuditMaxSize')

        if m.get('ResultAuditMode') is not None:
            self.result_audit_mode = m.get('ResultAuditMode')

        return self

