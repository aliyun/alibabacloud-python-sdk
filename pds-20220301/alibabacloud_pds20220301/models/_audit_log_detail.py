# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class AuditLogDetail(DaraModel):
    def __init__(
        self,
        drive_log_detail: main_models.DriveLogDetail = None,
        file_log_detail: main_models.FileLogDetail = None,
        user_log_detail: main_models.UserLogDetail = None,
    ):
        self.drive_log_detail = drive_log_detail
        self.file_log_detail = file_log_detail
        self.user_log_detail = user_log_detail

    def validate(self):
        if self.drive_log_detail:
            self.drive_log_detail.validate()
        if self.file_log_detail:
            self.file_log_detail.validate()
        if self.user_log_detail:
            self.user_log_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_log_detail is not None:
            result['drive_log_detail'] = self.drive_log_detail.to_map()

        if self.file_log_detail is not None:
            result['file_log_detail'] = self.file_log_detail.to_map()

        if self.user_log_detail is not None:
            result['user_log_detail'] = self.user_log_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_log_detail') is not None:
            temp_model = main_models.DriveLogDetail()
            self.drive_log_detail = temp_model.from_map(m.get('drive_log_detail'))

        if m.get('file_log_detail') is not None:
            temp_model = main_models.FileLogDetail()
            self.file_log_detail = temp_model.from_map(m.get('file_log_detail'))

        if m.get('user_log_detail') is not None:
            temp_model = main_models.UserLogDetail()
            self.user_log_detail = temp_model.from_map(m.get('user_log_detail'))

        return self

