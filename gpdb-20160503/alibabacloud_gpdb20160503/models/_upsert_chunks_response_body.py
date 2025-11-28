# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpsertChunksResponseBody(DaraModel):
    def __init__(
        self,
        embedding_tokens: str = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The number of tokens that are consumed during vectorization.
        # 
        # > A token is the minimum unit for splitting text. A token can be a word, phrase, punctuation, or character.
        self.embedding_tokens = embedding_tokens
        # The job ID. You can use the `GetGraphRAGJob` to view the job status.
        # 
        # > This parameter is returned only when the knowledge base is enabled.
        self.job_id = job_id
        # The response message.
        self.message = message
        # The unique ID of the request.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

