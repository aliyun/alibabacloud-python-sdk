# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class GetIndexJobStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIndexJobStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetIndexJobStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetIndexJobStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        documents: List[main_models.GetIndexJobStatusResponseBodyDataDocuments] = None,
        job_id: str = None,
        status: str = None,
    ):
        # The list of imported documents.
        self.documents = documents
        # The ID of the job.
        self.job_id = job_id
        # The status of the knowledge base job. Valid values:
        # 
        # *   COMPLETED
        # *   FAILED
        # *   RUNNING
        # *   PENDING
        self.status = status

    def validate(self):
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.GetIndexJobStatusResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetIndexJobStatusResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        code: str = None,
        doc_id: str = None,
        doc_name: str = None,
        gmt_modified: int = None,
        message: str = None,
        status: str = None,
    ):
        # HTTP status code
        self.code = code
        # The primary key ID of the document.
        self.doc_id = doc_id
        # The name of the document.
        self.doc_name = doc_name
        self.gmt_modified = gmt_modified
        # The error message.
        self.message = message
        # The import status of the document. Valid values:
        # 
        # *   INSERT_ERROR
        # *   RUNNING
        # *   DELETED
        # *   FINISH
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

