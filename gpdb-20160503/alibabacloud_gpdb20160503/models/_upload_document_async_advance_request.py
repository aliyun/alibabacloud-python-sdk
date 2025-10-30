# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO, Dict, Any, List

from darabonba.model import DaraModel

class UploadDocumentAsyncAdvanceRequest(DaraModel):
    def __init__(
        self,
        chunk_overlap: int = None,
        chunk_size: int = None,
        collection: str = None,
        dbinstance_id: str = None,
        document_loader_name: str = None,
        dry_run: bool = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        metadata: Dict[str, Any] = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        separators: List[str] = None,
        splitter_model: str = None,
        text_splitter_name: str = None,
        vl_enhance: bool = None,
        zh_title_enhance: bool = None,
    ):
        # The size of data that is overlapped between consecutive chunks. The maximum value of this parameter cannot be greater than the value of the ChunkSize parameter.
        # 
        # >  This parameter is used to prevent context missing that may occur due to data truncation. For example, when you upload a long text, you can retain specific overlapped text content between consecutive chunks to better understand the context.
        self.chunk_overlap = chunk_overlap
        # Strategy for processing large data: the size of each chunk when the data is split into smaller parts. Maximum value is 2048.
        self.chunk_size = chunk_size
        # The name of the document library. 
        # > Created by the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) API. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) API to view the document libraries that have already been created.
        # 
        # This parameter is required.
        self.collection = collection
        # Instance ID with vector engine optimization acceleration enabled. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) API to view details of all AnalyticDB PostgreSQL instances in the target region, including the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the document loader. You do not need to specify this parameter. A document loader is automatically specified based on the file extension. Valid values:
        # 
        # *   UnstructuredHTMLLoader: `.html`
        # *   UnstructuredMarkdownLoader: `.md`
        # *   PyMuPDFLoader: `.pdf`
        # *   PyPDFLoader: `.pdf`
        # *   RapidOCRPDFLoader: `.pdf`
        # *   PDFWithImageRefLoader: `.pdf` (with the text-image association feature)
        # *   JSONLoader: `.json`
        # *   CSVLoader: `.csv`
        # *   RapidOCRLoader: `.png`, `.jpg`, `.jpeg`, and `.bmp`
        # *   UnstructuredFileLoader: `.eml`, `.msg`, `.rst`, `.txt`, `.docx`, `.epub`, `.odt`, `.pptx`, and `.tsv`
        self.document_loader_name = document_loader_name
        # Specifies whether to perform only document understanding and chunking, but not vectorization and storage. Default value: false.
        # 
        # >  You can set this parameter to true, check the chunking effect, and then perform optimization if needed.
        self.dry_run = dry_run
        # The file name of the document.
        # 
        # > 
        # 
        # *   We recommend that you add an extension to the file name. Examples: `.json`, `.md`, and `.pdf`. If you do not add an extension, the default loader designed for unstructured data is used.
        # 
        # *   If an image file is involved, the file name must contain an extension. The following extensions are supported: `.bmp`, `.jpg`, `.jpeg`, `.png`, and `.tiff`.
        # 
        # *   You can use a compressed package to upload images. The package file name must contain an extension. Supported package file extensions: `.tar`, `.gz`, and `.zip`.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The URL of the publicly accessible document.
        # >  > - It is recommended to call this interface using the SDK, which provides a method called UploadDocumentAsyncAdvance for directly uploading local files. > - If the URL points to an image archive, the number of images in the archive should not exceed 100.
        # 
        # This parameter is required.
        self.file_url_object = file_url_object
        # The metadata. The value of this parameter must be the same as the Metadata parameter that is specified when you call the CreateDocumentCollection operation.
        self.metadata = metadata
        # Namespace, default is public. You can create one through the CreateNamespace interface and view the list via the ListNamespaces interface.
        self.namespace = namespace
        # The password corresponding to the namespace.  > This value is specified by the CreateNamespace interface.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The separators that are used to split large amounts of data.
        # 
        # > 
        # 
        # *   This is an important parameter that determines the chunking effect. This parameter is related to the splitter that is specified by the TextSplitterName parameter.
        # 
        # *   In most cases, you do not need to specify this parameter. The server assigns separators based on the value of the TextSplitterName parameter.
        self.separators = separators
        self.splitter_model = splitter_model
        # The name of the splitter. Valid values:
        # 
        # *   **ChineseRecursiveTextSplitter**: inherits from RecursiveCharacterTextSplitter, uses `["\\n\\n","\\n", "。|!|?", "\\.\\s|\\!\\s|\\?\\s", ";|;\\s", ",|,\\s"]` as separators by default, and uses regular expressions to match text.
        # *   **RecursiveCharacterTextSplitter**: uses `["\\n\\n", "\\n", " ", ""]` as separators by default. The splitter supports splitting code in languages such as `C++, Go, Java, JS, PHP, Proto, Python, RST, Ruby, Rust, Scala, Swift, Markdown, LaTeX, HTML, Sol, and C Sharp`.
        # *   **SpacyTextSplitter**: uses `\\n\\n` as separators by default and uses the en_core_web_sm model of spaCy. The splitter can obtain better splitting effect.
        # *   **MarkdownHeaderTextSplitter**: splits text in the `[("#", "head1"), ("##", "head2"), ("###", "head3"), ("####", "head4")]` format. The splitter is suitable for Markdown text.
        self.text_splitter_name = text_splitter_name
        self.vl_enhance = vl_enhance
        # Specifies whether to enable title enhancement.
        # 
        # >  You can determine the title text, mark the text in the metadata, and then combine the text with the upper-level title to implement text enhancement.
        self.zh_title_enhance = zh_title_enhance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_overlap is not None:
            result['ChunkOverlap'] = self.chunk_overlap

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.document_loader_name is not None:
            result['DocumentLoaderName'] = self.document_loader_name

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.separators is not None:
            result['Separators'] = self.separators

        if self.splitter_model is not None:
            result['SplitterModel'] = self.splitter_model

        if self.text_splitter_name is not None:
            result['TextSplitterName'] = self.text_splitter_name

        if self.vl_enhance is not None:
            result['VlEnhance'] = self.vl_enhance

        if self.zh_title_enhance is not None:
            result['ZhTitleEnhance'] = self.zh_title_enhance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkOverlap') is not None:
            self.chunk_overlap = m.get('ChunkOverlap')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DocumentLoaderName') is not None:
            self.document_loader_name = m.get('DocumentLoaderName')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Separators') is not None:
            self.separators = m.get('Separators')

        if m.get('SplitterModel') is not None:
            self.splitter_model = m.get('SplitterModel')

        if m.get('TextSplitterName') is not None:
            self.text_splitter_name = m.get('TextSplitterName')

        if m.get('VlEnhance') is not None:
            self.vl_enhance = m.get('VlEnhance')

        if m.get('ZhTitleEnhance') is not None:
            self.zh_title_enhance = m.get('ZhTitleEnhance')

        return self

