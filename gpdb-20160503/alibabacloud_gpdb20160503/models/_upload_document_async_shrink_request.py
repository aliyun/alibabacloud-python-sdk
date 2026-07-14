# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadDocumentAsyncShrinkRequest(DaraModel):
    def __init__(
        self,
        chunk_overlap: int = None,
        chunk_size: int = None,
        collection: str = None,
        dbinstance_id: str = None,
        document_loader_name: str = None,
        dry_run: bool = None,
        file_name: str = None,
        file_url: str = None,
        metadata_shrink: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        separators_shrink: str = None,
        splitter_model: str = None,
        text_splitter_name: str = None,
        vl_enhance: bool = None,
        zh_title_enhance: bool = None,
    ):
        # The size of overlapping data between consecutive chunks. The maximum value of this parameter cannot be greater than the value of the ChunkSize parameter.
        # >  This parameter prevents context loss caused by data truncation. For example, when you upload long text, you can retain specific overlapping text content between consecutive chunks for better context understanding.
        self.chunk_overlap = chunk_overlap
        # The strategy for processing large data: the size of each chunk when data is split into smaller parts. Maximum value: 2048.
        self.chunk_size = chunk_size
        # The name of the document collection.
        # >Created by the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to query the created document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The ID of the instance that has vector engine optimization enabled. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in the target region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the document loader. If you do not specify this parameter, the system automatically selects the corresponding document loader based on the file name extension in the following order. Valid values:
        # *   UnstructuredHTMLLoader: .html
        # *   UnstructuredMarkdownLoader: .md
        # *   PyMuPDFLoader: .pdf
        # *   PyPDFLoader: .pdf
        # *   RapidOCRPDFLoader: .pdf
        # *   PDFWithImageRefLoader: .pdf (with the text-image association feature)
        # *   JSONLoader: .json
        # *   CSVLoader: .csv
        # *   RapidOCRLoader: .png, .jpg, .jpeg, and .bmp
        # *   UnstructuredFileLoader: .eml, .msg, .rst, .txt, .docx, .epub, .odt, .pptx, and .tsv
        # *   ADBPGLoader (paid, first 3,000 pages free): .pdf, .doc, .docx, .ppt, .pptx, .xls, .xlsx, .xlsm, .csv, .txt, .jpg, .jpeg, .png, .bmp, .gif, .md, .html, .epub, .mobi, and .rtf
        self.document_loader_name = document_loader_name
        # Specifies whether to perform only document understanding and chunking without vectorization and storage. Default value: false.
        # 
        # >  You can set this parameter to true to check the chunking results and then optimize as needed.
        self.dry_run = dry_run
        # The file name of the document.
        # 
        # >* The file name must include file name extension, such as .json, .md, or .pdf.
        # >* Supported image file extensions include .bmp, .jpg, .jpeg, .png, and .tiff.
        # >* You can upload images by using an archive. The archive file name must include file name extension. Supported archive extensions include .tar, .gz, and .zip.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The publicly accessible URL of the document.
        # > Use the SDK to call this operation. The SDK provides a method named UploadDocumentAsyncAdvance that allows you to directly upload local files.
        # If the URL points to an image archive, the number of images in the archive cannot exceed 100.
        # 
        # >Notice: 
        # The maximum size of an image uploaded by using multimodal-embedding-v1 is 3 MB.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The metadata. The value of this parameter must be the same as the Metadata parameter specified when you call the CreateDocumentCollection operation.
        self.metadata_shrink = metadata_shrink
        # The namespace. Default value: public. You can call the CreateNamespace operation to create a namespace and call the ListNamespaces operation to query the list of namespaces.
        self.namespace = namespace
        # The password of the namespace. The value is specified by the CreateNamespace operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The separators used to split large data.
        # > *   This is an important parameter that determines the effectiveness of data chunking. This parameter is related to the splitter specified by the TextSplitterName parameter.
        # >*  In most cases, you do not need to specify this parameter. The server assigns separators based on the value of the TextSplitterName parameter.
        self.separators_shrink = separators_shrink
        # The splitting model to use when DocumentLoaderName is set to ADBPGLoader and TextSplitterName is set to LLMSplitter. Default value: qwen3-8b.
        # > 
        # > Currently supported splitting models:
        # > qwq-plus, qwq-plus-latest,
        # > qwen-max, qwen-max-latest,
        # > qwen-plus, qwen-plus-latest,
        # > qwen-turbo, qwen-turbo-latest,
        # > qwen3-235b-a22b, qwen3-32b, qwen3-30b-a3b,
        # > qwen3-14b, qwen3-8b, qwen3-4b, qwen3-1.7b, qwen3-0.6b,
        # > qwq-32b
        # > qwen2.5-14b-instruct-1m, qwen2.5-7b-instruct-1m
        # > qwen2.5-72b-instruct, qwen2.5-32b-instruct,
        # > qwen2.5-14b-instruct, qwen2.5-7b-instruct,
        # > qwen2.5-3b-instruct, qwen2.5-1.5b-instruct, qwen2.5-0.5b-instruct
        self.splitter_model = splitter_model
        # The name of the text splitter. Valid values:
        # *   **ChineseRecursiveTextSplitter**: inherits from RecursiveCharacterTextSplitter and uses `["
        # 
        # ","
        # ", "。|!|?", "\\.\\s|\\!\\s|\\?\\s", ";|;\\s", ",|,\\s"]` as the default separators with regular expression matching.
        # *   **RecursiveCharacterTextSplitter**: uses `["
        # 
        # ", "
        # ", " ", ""]` as the default separators. This splitter supports splitting code in languages such as C++, Go, Java, JS, PHP, Proto, Python, RST, Ruby, Rust, Scala, Swift, Markdown, LaTeX, HTML, Sol, and C Sharp.
        # *   **SpacyTextSplitter**: uses `
        # 
        # ` as the default separator and the spaCy en_core_web_sm model. This splitter provides better splitting results.
        # *   **MarkdownHeaderTextSplitter**: splits text in the format of [("#", "head1"), ("##", "head2"), ("###", "head3"), ("####", "head4")]. This splitter is suitable for Markdown text.
        # *   **LLMSplitter**: uses an LLM to split text. The default model is qwen3-8b. This splitter takes effect only when ADBPGLoader is selected as the document loader.
        self.text_splitter_name = text_splitter_name
        # Specifies whether to enable VL-enhanced content recognition for complex documents. Default value: false.
        # 
        # > 
        # > - For complex documents with disorganized layouts and formats, enable VL-enhanced content recognition.
        # > - After VL-enhanced content recognition is enabled, document processing takes longer.
        # > - After VL-enhanced content recognition is enabled, images in the document cannot be stored or recalled.
        self.vl_enhance = vl_enhance
        # Specifies whether to enable title enhancement.
        # >You can identify the title text, mark the text in the metadata, and then combine the text with the upper-level title for text enhancement.
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

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.metadata_shrink is not None:
            result['Metadata'] = self.metadata_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.separators_shrink is not None:
            result['Separators'] = self.separators_shrink

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
            self.file_url = m.get('FileUrl')

        if m.get('Metadata') is not None:
            self.metadata_shrink = m.get('Metadata')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Separators') is not None:
            self.separators_shrink = m.get('Separators')

        if m.get('SplitterModel') is not None:
            self.splitter_model = m.get('SplitterModel')

        if m.get('TextSplitterName') is not None:
            self.text_splitter_name = m.get('TextSplitterName')

        if m.get('VlEnhance') is not None:
            self.vl_enhance = m.get('VlEnhance')

        if m.get('ZhTitleEnhance') is not None:
            self.zh_title_enhance = m.get('ZhTitleEnhance')

        return self

