# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ForkKnowledgeFileResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ForkKnowledgeFileResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ForkKnowledgeFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ForkKnowledgeFileResponseBodyData(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_location: str = None,
        message: str = None,
        owner_file_id: str = None,
        process_status: str = None,
        source_file_id: str = None,
        success: bool = None,
    ):
        # The ID of the newly created reference record, represented as a decimal string. Use this ID for subsequent management of the record. This parameter is returned only when the operation is successful.
        self.file_id = file_id
        # The address of the new reference record, in the format of fork://<source file ID>/<new file ID>. This parameter is returned only when the operation is successful.
        self.file_location = file_location
        # The description of the operation result. If the business operation fails, this parameter indicates the cause or the security error code.
        self.message = message
        # The ID of the content host file, represented as a decimal string. Currently, this value is the same as the source file ID. This parameter is returned only when the operation is successful.
        self.owner_file_id = owner_file_id
        # The status of the new reference record. The value is fixed to DUPLICATED. This parameter is returned only when the operation is successful.
        self.process_status = process_status
        # The ID of the source file, represented as a decimal string. This parameter is returned only when the operation is successful.
        self.source_file_id = source_file_id
        # Indicates whether the business operation is successful. If the operation fails, the Data parameter contains only Success and Message.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.message is not None:
            result['Message'] = self.message

        if self.owner_file_id is not None:
            result['OwnerFileId'] = self.owner_file_id

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.source_file_id is not None:
            result['SourceFileId'] = self.source_file_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OwnerFileId') is not None:
            self.owner_file_id = m.get('OwnerFileId')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('SourceFileId') is not None:
            self.source_file_id = m.get('SourceFileId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

