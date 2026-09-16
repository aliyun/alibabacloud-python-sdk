# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBaseDocument(DaraModel):
    def __init__(
        self,
        chunk_configuration: main_models.KnowledgeBaseDocumentChunkConfiguration = None,
        chunk_count: int = None,
        created_at: str = None,
        document_id: str = None,
        error_code: str = None,
        error_message: str = None,
        file_name: str = None,
        file_size: int = None,
        metadata: List[main_models.KnowledgeBaseDocumentMetadata] = None,
        source_modified_time: int = None,
        source_type: str = None,
        source_uri: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The snapshot of the document-level chunking policy actually used for this document. This field is returned only if ChunkConfiguration was explicitly specified during upload (BeginUpload) or update (UpdateDocument). If not specified, the document is chunked based on the knowledge base-level default configurations, and this field is not returned. The knowledge base-level configuration is not echoed back to avoid misleading users about the actual chunking basis for this document when the knowledge base-level configuration is subsequently changed.
        self.chunk_configuration = chunk_configuration
        # The number of chunks generated after processing is complete.
        self.chunk_count = chunk_count
        # The time when the document was created.
        self.created_at = created_at
        # The unique identifier of the document.
        self.document_id = document_id
        # The stable error code returned when processing fails.
        self.error_code = error_code
        # The desensitized error message returned when processing fails.
        self.error_message = error_message
        # The file name of the document.
        self.file_name = file_name
        # The file size of the document, in bytes.
        self.file_size = file_size
        # The document-level metadata key-value pairs, including constant field values and system variable values. This field is not returned if no metadata is specified.
        self.metadata = metadata
        # The last modification time in the upstream source system, in epoch milliseconds. This field is empty if no source information is available.
        self.source_modified_time = source_modified_time
        # The delivery channel through which the document entered the knowledge base. This value is written by the system and cannot be specified by users. Valid values:
        # - UPLOAD: manually uploaded through the console or API.
        # - OSS: imported through an OSS event stream.
        # 
        # New values may be added when new channels are supported. The values are not restricted to a fixed enumeration.
        self.source_type = source_type
        # The original source address of the document, such as oss://bucket/path/file.md. This field may be empty for manually uploaded documents.
        self.source_uri = source_uri
        # The processing status of the document. Valid values:
        # - UPLOADING: uploading in progress.
        # - PENDING: upload complete and queued for processing. This is typically a transitional state that lasts for seconds.
        # - PROCESSING: parsing and processing in progress.
        # - COMPLETED: processing complete and searchable.
        # - FAILED: processing failed.
        # - DELETING: deletion in progress.
        self.status = status
        # The time when the document was last updated.
        self.updated_at = updated_at

    def validate(self):
        if self.chunk_configuration:
            self.chunk_configuration.validate()
        if self.metadata:
            for v1 in self.metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_configuration is not None:
            result['ChunkConfiguration'] = self.chunk_configuration.to_map()

        if self.chunk_count is not None:
            result['ChunkCount'] = self.chunk_count

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        result['Metadata'] = []
        if self.metadata is not None:
            for k1 in self.metadata:
                result['Metadata'].append(k1.to_map() if k1 else None)

        if self.source_modified_time is not None:
            result['SourceModifiedTime'] = self.source_modified_time

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkConfiguration') is not None:
            temp_model = main_models.KnowledgeBaseDocumentChunkConfiguration()
            self.chunk_configuration = temp_model.from_map(m.get('ChunkConfiguration'))

        if m.get('ChunkCount') is not None:
            self.chunk_count = m.get('ChunkCount')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        self.metadata = []
        if m.get('Metadata') is not None:
            for k1 in m.get('Metadata'):
                temp_model = main_models.KnowledgeBaseDocumentMetadata()
                self.metadata.append(temp_model.from_map(k1))

        if m.get('SourceModifiedTime') is not None:
            self.source_modified_time = m.get('SourceModifiedTime')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

class KnowledgeBaseDocumentMetadata(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The metadata field name.
        self.key = key
        # The metadata field value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class KnowledgeBaseDocumentChunkConfiguration(DaraModel):
    def __init__(
        self,
        heading_level: int = None,
        max_chunk_size: int = None,
        overlap_size: int = None,
        preprocess_rules: main_models.KnowledgeBaseDocumentChunkConfigurationPreprocessRules = None,
        separator: str = None,
        strategy: str = None,
    ):
        # The heading level (1 to 6) used for splitting in the BY_HEADING strategy. Headings at or above this level serve as split boundaries. Deeper-level headings are retained in the chunk body.
        self.heading_level = heading_level
        # The maximum character length of a single chunk. Starting from revision 22, this value is character-based. Valid values: 1 to 6000.
        self.max_chunk_size = max_chunk_size
        # The overlap character length between adjacent chunks. This parameter takes effect only for the BY_LENGTH strategy. If the value is greater than 0, the beginning of the next chunk repeats the content from the end of the previous chunk within this window. The overlap does not cause a chunk to exceed MaxChunkSize. A value of 0 indicates no overlap.
        self.overlap_size = overlap_size
        # The snapshot of preprocessing rules.
        self.preprocess_rules = preprocess_rules
        # The separator used in the BY_SEPARATOR strategy. The separator is matched as a literal string (not a regular expression). The maximum length is 32 characters.
        self.separator = separator
        # The chunking strategy. Valid values:
        # - AUTO: intelligent splitting (heading-aware + paragraph packing).
        # - BY_LENGTH: sliding window splitting by length. You can specify OverlapSize.
        # - BY_SEPARATOR: splitting by separator. You must specify Separator.
        # - BY_HEADING: splitting by heading level. You must specify HeadingLevel.
        self.strategy = strategy

    def validate(self):
        if self.preprocess_rules:
            self.preprocess_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.heading_level is not None:
            result['HeadingLevel'] = self.heading_level

        if self.max_chunk_size is not None:
            result['MaxChunkSize'] = self.max_chunk_size

        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size

        if self.preprocess_rules is not None:
            result['PreprocessRules'] = self.preprocess_rules.to_map()

        if self.separator is not None:
            result['Separator'] = self.separator

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeadingLevel') is not None:
            self.heading_level = m.get('HeadingLevel')

        if m.get('MaxChunkSize') is not None:
            self.max_chunk_size = m.get('MaxChunkSize')

        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')

        if m.get('PreprocessRules') is not None:
            temp_model = main_models.KnowledgeBaseDocumentChunkConfigurationPreprocessRules()
            self.preprocess_rules = temp_model.from_map(m.get('PreprocessRules'))

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class KnowledgeBaseDocumentChunkConfigurationPreprocessRules(DaraModel):
    def __init__(
        self,
        remove_urls_and_emails: bool = None,
        replace_consecutive_whitespace: bool = None,
    ):
        # Specifies whether to remove URLs and email addresses during parsing.
        self.remove_urls_and_emails = remove_urls_and_emails
        # Specifies whether to replace consecutive whitespace characters (spaces, line breaks, and tab characters) with a single space.
        self.replace_consecutive_whitespace = replace_consecutive_whitespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remove_urls_and_emails is not None:
            result['RemoveUrlsAndEmails'] = self.remove_urls_and_emails

        if self.replace_consecutive_whitespace is not None:
            result['ReplaceConsecutiveWhitespace'] = self.replace_consecutive_whitespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoveUrlsAndEmails') is not None:
            self.remove_urls_and_emails = m.get('RemoveUrlsAndEmails')

        if m.get('ReplaceConsecutiveWhitespace') is not None:
            self.replace_consecutive_whitespace = m.get('ReplaceConsecutiveWhitespace')

        return self

