# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetGraphRAGJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetGraphRAGJobResponseBodyJob = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        usage: main_models.GetGraphRAGJobResponseBodyUsage = None,
    ):
        # The details of the task for building a knowledge graph.
        self.job = job
        # The additional information that is returned.
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
        if self.job:
            self.job.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Job') is not None:
            temp_model = main_models.GetGraphRAGJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Usage') is not None:
            temp_model = main_models.GetGraphRAGJobResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class GetGraphRAGJobResponseBodyUsage(DaraModel):
    def __init__(
        self,
        embedding_tokens: int = None,
        llminput_tokens: int = None,
        llmoutput_tokens: int = None,
    ):
        # The number of tokens that are consumed during vectorization.
        # 
        # > A token is the minimum unit for splitting text. A token can be a word, phrase, punctuation, or character.
        self.embedding_tokens = embedding_tokens
        # The number of tokens used by the large model input.
        self.llminput_tokens = llminput_tokens
        # The number of tokens used for large model output.
        self.llmoutput_tokens = llmoutput_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        if self.llminput_tokens is not None:
            result['LLMInputTokens'] = self.llminput_tokens

        if self.llmoutput_tokens is not None:
            result['LLMOutputTokens'] = self.llmoutput_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        if m.get('LLMInputTokens') is not None:
            self.llminput_tokens = m.get('LLMInputTokens')

        if m.get('LLMOutputTokens') is not None:
            self.llmoutput_tokens = m.get('LLMOutputTokens')

        return self

class GetGraphRAGJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        id: str = None,
        progress: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # Indicates whether the operation is complete.
        self.completed = completed
        # The job creation time.
        self.create_time = create_time
        # The error message that is returned when the current operation is abnormal or fails.
        self.error = error
        # The job ID.
        self.id = id
        # The progress of the document upload job. Unit: %. A value of 100 indicates that the job is complete.
        self.progress = progress
        # The state of the job. Valid values:
        # 
        # *   **Success**
        # *   **Failed** (See the Error parameter for failure reasons.)
        # *   **Running**
        # *   **Pending**
        self.status = status
        # The job last updated time.
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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

