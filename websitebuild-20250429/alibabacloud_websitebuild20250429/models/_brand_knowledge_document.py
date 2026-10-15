# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BrandKnowledgeDocument(DaraModel):
    def __init__(
        self,
        content_sufficient: bool = None,
        content_type: str = None,
        created_at: int = None,
        deletable: bool = None,
        display_title: str = None,
        doc_category: str = None,
        document_id: str = None,
        error_code: str = None,
        error_message: str = None,
        file_size: int = None,
        key_topics: List[str] = None,
        one_line_summary: str = None,
        original_name: str = None,
        project_id: str = None,
        ready_at: int = None,
        status: str = None,
        status_message: str = None,
        summary_error_code: str = None,
        summary_status: str = None,
        updated_at: int = None,
    ):
        # Specifies whether the content is sufficient to be considered for plan summary candidates.
        self.content_sufficient = content_sufficient
        # The MIME type of the file.
        self.content_type = content_type
        # The creation time in Unix milliseconds.
        self.created_at = created_at
        # Specifies whether deletion is currently allowed.
        self.deletable = deletable
        # The display title.
        self.display_title = display_title
        # The document category.
        self.doc_category = doc_category
        # The ID of the brand knowledge document.
        self.document_id = document_id
        # The stable error code for main processing failures.
        self.error_code = error_code
        # The desensitized error message for main processing failures.
        self.error_message = error_message
        # The file size in bytes.
        self.file_size = file_size
        # The summary keywords.
        self.key_topics = key_topics
        # The one-line summary, which is used only to construct search queries and cannot be used as factual evidence.
        self.one_line_summary = one_line_summary
        # The original file name.
        self.original_name = original_name
        # The ID of the business workspace. For GEO business workspaces of the brand marketing type, this is the appWorkspaceId.
        self.project_id = project_id
        # The time when the document is ready for reference, in Unix milliseconds.
        self.ready_at = ready_at
        # The document processing status.
        self.status = status
        # The message displayed on the status page.
        self.status_message = status_message
        # The stable error code for summary failures.
        self.summary_error_code = summary_error_code
        # The summary status.
        self.summary_status = summary_status
        # The last update time in Unix milliseconds.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_sufficient is not None:
            result['ContentSufficient'] = self.content_sufficient

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.deletable is not None:
            result['Deletable'] = self.deletable

        if self.display_title is not None:
            result['DisplayTitle'] = self.display_title

        if self.doc_category is not None:
            result['DocCategory'] = self.doc_category

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.key_topics is not None:
            result['KeyTopics'] = self.key_topics

        if self.one_line_summary is not None:
            result['OneLineSummary'] = self.one_line_summary

        if self.original_name is not None:
            result['OriginalName'] = self.original_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.ready_at is not None:
            result['ReadyAt'] = self.ready_at

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.summary_error_code is not None:
            result['SummaryErrorCode'] = self.summary_error_code

        if self.summary_status is not None:
            result['SummaryStatus'] = self.summary_status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSufficient') is not None:
            self.content_sufficient = m.get('ContentSufficient')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')

        if m.get('DisplayTitle') is not None:
            self.display_title = m.get('DisplayTitle')

        if m.get('DocCategory') is not None:
            self.doc_category = m.get('DocCategory')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('KeyTopics') is not None:
            self.key_topics = m.get('KeyTopics')

        if m.get('OneLineSummary') is not None:
            self.one_line_summary = m.get('OneLineSummary')

        if m.get('OriginalName') is not None:
            self.original_name = m.get('OriginalName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ReadyAt') is not None:
            self.ready_at = m.get('ReadyAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('SummaryErrorCode') is not None:
            self.summary_error_code = m.get('SummaryErrorCode')

        if m.get('SummaryStatus') is not None:
            self.summary_status = m.get('SummaryStatus')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

