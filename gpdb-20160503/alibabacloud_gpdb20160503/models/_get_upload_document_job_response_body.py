# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetUploadDocumentJobResponseBody(DaraModel):
    def __init__(
        self,
        chunk_result: main_models.GetUploadDocumentJobResponseBodyChunkResult = None,
        job: main_models.GetUploadDocumentJobResponseBodyJob = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        usage: main_models.GetUploadDocumentJobResponseBodyUsage = None,
    ):
        # The chunking result.
        self.chunk_result = chunk_result
        # The information about the document upload job.
        self.job = job
        # The returned message.
        self.message = message
        # The unique ID of the request.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status
        # The number of tokens that are consumed by document understanding or embedding.
        self.usage = usage

    def validate(self):
        if self.chunk_result:
            self.chunk_result.validate()
        if self.job:
            self.job.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_result is not None:
            result['ChunkResult'] = self.chunk_result.to_map()

        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkResult') is not None:
            temp_model = main_models.GetUploadDocumentJobResponseBodyChunkResult()
            self.chunk_result = temp_model.from_map(m.get('ChunkResult'))

        if m.get('Job') is not None:
            temp_model = main_models.GetUploadDocumentJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Usage') is not None:
            temp_model = main_models.GetUploadDocumentJobResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class GetUploadDocumentJobResponseBodyUsage(DaraModel):
    def __init__(
        self,
        embedding_entries: int = None,
        embedding_tokens: int = None,
    ):
        # The number of entries during vectorization.
        self.embedding_entries = embedding_entries
        # The number of tokens that are consumed during vectorization.
        # 
        # > A token is the minimum unit for splitting text. A token can be a word, phrase, punctuation, or character.
        self.embedding_tokens = embedding_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_entries is not None:
            result['EmbeddingEntries'] = self.embedding_entries

        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingEntries') is not None:
            self.embedding_entries = m.get('EmbeddingEntries')

        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        return self

class GetUploadDocumentJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        error_code: str = None,
        id: str = None,
        progress: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # Indicates whether the operation is complete.
        self.completed = completed
        # Job creation time.
        self.create_time = create_time
        # The error message that is returned when the current operation is abnormal or fails.
        self.error = error
        # The error code returned.
        self.error_code = error_code
        # The job ID.
        self.id = id
        # The progress of the document upload job. Unit: %. A value of 100 indicates that the job is complete.
        self.progress = progress
        # The status of the job. Valid values:
        # 
        # *   Success
        # *   Failed (See the Error parameter for failure reasons.)
        # *   Cancelling
        # *   Cancelled
        # *   Start
        # *   Running
        # *   Pending
        self.status = status
        # Job last updated time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed is not None:
            result['Completed'] = self.completed

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error is not None:
            result['Error'] = self.error

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.id is not None:
            result['Id'] = self.id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetUploadDocumentJobResponseBodyChunkResult(DaraModel):
    def __init__(
        self,
        chunk_file_url: str = None,
        document_loader_result_file_url: str = None,
        plain_chunk_file_url: str = None,
    ):
        # The URL of the file after chunking. The validity period of the URL is 2 hours. The file is in the JSONL format. Each line is in the `{"page_content":"*****", "metadata": {"**":"***","**":"***"}` format.
        self.chunk_file_url = chunk_file_url
        # The markdown output file that is generated by the ADBPGLoader. The validity period is 2 hours.
        self.document_loader_result_file_url = document_loader_result_file_url
        # The URL of the file that does not contain metadata after chunking. The validity period of the URL is 2 hours. The file is in the TXT format. Each line is a chunk. The file can be easily used for embedding.
        self.plain_chunk_file_url = plain_chunk_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_file_url is not None:
            result['ChunkFileUrl'] = self.chunk_file_url

        if self.document_loader_result_file_url is not None:
            result['DocumentLoaderResultFileUrl'] = self.document_loader_result_file_url

        if self.plain_chunk_file_url is not None:
            result['PlainChunkFileUrl'] = self.plain_chunk_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkFileUrl') is not None:
            self.chunk_file_url = m.get('ChunkFileUrl')

        if m.get('DocumentLoaderResultFileUrl') is not None:
            self.document_loader_result_file_url = m.get('DocumentLoaderResultFileUrl')

        if m.get('PlainChunkFileUrl') is not None:
            self.plain_chunk_file_url = m.get('PlainChunkFileUrl')

        return self

