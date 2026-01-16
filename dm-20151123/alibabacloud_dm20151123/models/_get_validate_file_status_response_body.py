# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetValidateFileStatusResponseBody(DaraModel):
    def __init__(
        self,
        catch_all_num: str = None,
        complete_time: str = None,
        do_not_mail_num: str = None,
        file_id: str = None,
        file_name: str = None,
        invalid_num: str = None,
        percentage: str = None,
        processed_num: str = None,
        request_id: str = None,
        status: str = None,
        total_num: str = None,
        unknown_num: str = None,
        upload_time: str = None,
        valid_num: str = None,
    ):
        self.catch_all_num = catch_all_num
        self.complete_time = complete_time
        self.do_not_mail_num = do_not_mail_num
        self.file_id = file_id
        self.file_name = file_name
        self.invalid_num = invalid_num
        self.percentage = percentage
        self.processed_num = processed_num
        self.request_id = request_id
        self.status = status
        self.total_num = total_num
        self.unknown_num = unknown_num
        self.upload_time = upload_time
        self.valid_num = valid_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catch_all_num is not None:
            result['CatchAllNum'] = self.catch_all_num

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.do_not_mail_num is not None:
            result['DoNotMailNum'] = self.do_not_mail_num

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.invalid_num is not None:
            result['InvalidNum'] = self.invalid_num

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.processed_num is not None:
            result['ProcessedNum'] = self.processed_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.unknown_num is not None:
            result['UnknownNum'] = self.unknown_num

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.valid_num is not None:
            result['ValidNum'] = self.valid_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatchAllNum') is not None:
            self.catch_all_num = m.get('CatchAllNum')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('DoNotMailNum') is not None:
            self.do_not_mail_num = m.get('DoNotMailNum')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('InvalidNum') is not None:
            self.invalid_num = m.get('InvalidNum')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('ProcessedNum') is not None:
            self.processed_num = m.get('ProcessedNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('UnknownNum') is not None:
            self.unknown_num = m.get('UnknownNum')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('ValidNum') is not None:
            self.valid_num = m.get('ValidNum')

        return self

