# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOfficeConversionTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        end_page: int = None,
        first_page: bool = None,
        fit_to_height: bool = None,
        fit_to_width: bool = None,
        hold_line_feed: bool = None,
        image_dpi: int = None,
        long_picture: bool = None,
        long_text: bool = None,
        max_sheet_column: int = None,
        max_sheet_row: int = None,
        notification_shrink: str = None,
        pages: str = None,
        paper_horizontal: bool = None,
        paper_size: str = None,
        password: str = None,
        project_name: str = None,
        quality: int = None,
        scale_percentage: int = None,
        sheet_count: int = None,
        sheet_index: int = None,
        show_comments: bool = None,
        source_type: str = None,
        source_uri: str = None,
        sources_shrink: str = None,
        start_page: int = None,
        tags_shrink: str = None,
        target_type: str = None,
        target_uri: str = None,
        target_uriprefix: str = None,
        trim_policy_shrink: str = None,
        user_data: str = None,
    ):
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The chained authorization configuration. This parameter is not required. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The end page for the document conversion. The default value is -1, which indicates that all pages from the start page to the last page are converted.
        # 
        # > - If the source file is a spreadsheet, you must specify the worksheet number (\\`SheetIndex\\`).
        # >
        # > - If the document has many pages, we recommend that you convert them in batches. Otherwise, the conversion may time out.
        # >
        # > - This parameter takes effect only when you convert the document to images. It does not take effect when you convert the document to a PDF file or a text file.
        self.end_page = end_page
        # When you convert a spreadsheet document to images, specifies whether to return only the first image of the conversion result. The number of rows and columns in the image is the result of automatic splitting. Valid values:
        # 
        # - false (default): No. All images are returned.
        # 
        # - true: Yes. Only the first image is returned. This is used to extract a thumbnail.
        # 
        # > This parameter takes effect only if you set the **LongPicture** parameter to `true`.
        self.first_page = first_page
        # When you convert a spreadsheet document to images or a PDF file, specifies whether to render all rows on a single image or PDF page. Valid values:
        # 
        # - false (default): No. The content is rendered on multiple images or PDF pages.
        # 
        # - true: Yes. The content is rendered on a single image or PDF page.
        self.fit_to_height = fit_to_height
        # When you convert a spreadsheet document to images or a PDF file, specifies whether to render all columns on a single image or PDF page. Valid values:
        # 
        # - false (default): No. The content is rendered on multiple images or PDF pages.
        # 
        # - true: Yes. The content is rendered on a single image or PDF page.
        self.fit_to_width = fit_to_width
        # When you convert a document to text, specifies whether to keep the line feeds in the document. Valid values:
        # 
        # - false (default): No. Line feeds are not kept.
        # 
        # - true: Yes. Line feeds are kept.
        self.hold_line_feed = hold_line_feed
        # The DPI of the output image. Valid values: 96 to 600. The default value is 96.
        self.image_dpi = image_dpi
        # When you convert a document to images, specifies whether to convert it into a long image. Valid values:
        # 
        # - false (default): No. The document is converted into multiple images.
        # 
        # - true: Yes. The document is converted into a long image.
        # 
        # > You can combine a maximum of 20 pages into a long image. If the number of pages exceeds this limit, the conversion task may fail.
        self.long_picture = long_picture
        # When you convert a document to text, specifies whether to convert it into a long text file. Valid values:
        # 
        # - false (default): No. Each page of the document is converted into a separate text file.
        # 
        # - true: Yes. All content is placed in a single text file.
        self.long_text = long_text
        # The maximum number of columns to convert when you convert a spreadsheet document to images. By default, all columns are converted.
        # 
        # > This parameter takes effect only when you set **LongPicture** to `true`.
        self.max_sheet_column = max_sheet_column
        # The maximum number of rows to convert when you convert a spreadsheet document to images. By default, all rows are converted.
        # 
        # > This parameter takes effect only when you set **LongPicture** to `true`.
        self.max_sheet_row = max_sheet_row
        # The message notification configuration. For more information, click Notification. For more information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The page numbers to convert. This parameter has a higher priority than the \\`StartPage\\` and \\`EndPage\\` parameters. The format is as follows:
        # 
        # - Separate multiple page numbers with commas (,), for example, 1,2.
        # 
        # - Specify a range of consecutive pages with a hyphen (-), for example, 1,2-4,7.
        self.pages = pages
        # When you convert a spreadsheet document to images, specifies whether to place the paper horizontally. The output image is similar to a printed page. Valid values:
        # 
        # - false (default): No. The paper is placed vertically.
        # 
        # - true: Yes. The paper is placed horizontally.
        self.paper_horizontal = paper_horizontal
        # The paper size for converting a spreadsheet document to images. The output image is similar to a printed page. Valid values:
        # 
        # - A0
        # 
        # - A2
        # 
        # - A4 (default)
        # 
        # > This parameter takes effect only when you use it with the **FitToHeight** and **FitToWidth** parameters.
        self.paper_size = paper_size
        # The password to open the document. Set this parameter if you want to convert a password-protected document.
        self.password = password
        # The project name. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The quality of the converted file. Valid values: 0 to 100. A value of 0 indicates the lowest quality and the best performance. A value of 100 indicates the highest quality and the poorest performance. By default, the system sets an appropriate value based on the document content to balance quality and performance.
        self.quality = quality
        # The scaling ratio of the document. Valid values: 20 to 199. The default value is 100, which indicates that the document is not scaled.
        # 
        # > A value less than 100 indicates that the document is scaled down. A value greater than 100 indicates that the document is scaled up.
        self.scale_percentage = scale_percentage
        # The number of worksheets to convert to images in the spreadsheet document. By default, all worksheets are converted.
        self.sheet_count = sheet_count
        # The number of the worksheet to convert to images in the spreadsheet document. Valid values: 1 to the number of the last worksheet. The default value is 1.
        self.sheet_index = sheet_index
        # When you convert a word processor document to images, specifies whether to show comments. Valid values:
        # 
        # - false (default): No. Comments are not shown.
        # 
        # - true: Yes. Comments are shown.
        self.show_comments = show_comments
        # The extension type of the source data. By default, the type of the source data is determined by the extension of the OSS object. If the OSS object does not have an extension, you can set this parameter. Valid values:
        # 
        # - Word processor documents (Word): doc, docx, wps, wpss, docm, dotm, dot, and dotx
        # 
        # - Presentation documents (PowerPoint): pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss
        # 
        # - Spreadsheet documents (Excel): xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets
        # 
        # - PDF documents: pdf
        self.source_type = source_type
        # The storage address of the source data.
        # 
        # The OSS address must be in the oss\\://${Bucket}/${Object} format. \\`${Bucket}\\` is the name of the OSS bucket that is in the same region as the current project. \\`${Object}\\` is the full path of the file, including the file name extension.
        self.source_uri = source_uri
        # A list of input images. The images are converted in the order of their URIs in the list. (**This parameter is not yet published. Do not use it.**)
        self.sources_shrink = sources_shrink
        # The start page for the document conversion. The default value is 1.
        # 
        # > - If the source file is a spreadsheet, you must specify the worksheet number.
        # >
        # > - This parameter takes effect only when you convert the document to images. It does not take effect when you convert the document to a PDF file or a text file.
        self.start_page = start_page
        # The custom tags. The value is a dictionary. You can use tags to search for tasks.
        self.tags_shrink = tags_shrink
        # The type of the output file. Valid values:
        # 
        # - png: Converts the document to PNG images.
        # 
        # - jpg: Converts the document to JPG images.
        # 
        # - pdf: Converts the document to a PDF file.
        # 
        # - txt: Converts the document to a text-only file. This is mainly used to extract text content from the file. This option is supported only for presentation documents, word processor documents, and spreadsheet documents. When you convert a spreadsheet document, a single txt file is generated, and settings for sheet-related variables do not take effect.
        # 
        # This parameter is required.
        self.target_type = target_type
        # The template for the output address of the converted document.
        # 
        # The address must be in the `oss://{bucket}/{tags.custom}/{dirname}/{barename}.{autoext}` format. For more information, see [TargetURI templates](https://help.aliyun.com/document_detail/465762.html).
        # 
        # > Specify either this parameter or \\`TargetURIPrefix\\`.
        self.target_uri = target_uri
        # The prefix of the storage address for the output file after document conversion.
        # 
        # The prefix must be in the `oss://${Bucket}/${Prefix}/` format. \\`${Bucket}\\` is the name of the OSS bucket that is in the same region as the current project. \\`${Prefix}\\` is the prefix of the storage address for the output file.
        # 
        # > Specify either this parameter or \\`TargetURI\\`.
        self.target_uriprefix = target_uriprefix
        # The trimming policy for spreadsheet conversion. For example, if a spreadsheet contains many empty rows and columns, a large amount of white space may be generated if no trimming policy is specified.
        self.trim_policy_shrink = trim_policy_shrink
        # The custom information. This information is returned in the asynchronous notification message to help you associate the notification with your services. The value can be up to 2,048 bytes in length.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.end_page is not None:
            result['EndPage'] = self.end_page

        if self.first_page is not None:
            result['FirstPage'] = self.first_page

        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height

        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width

        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed

        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi

        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture

        if self.long_text is not None:
            result['LongText'] = self.long_text

        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column

        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.pages is not None:
            result['Pages'] = self.pages

        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal

        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size

        if self.password is not None:
            result['Password'] = self.password

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage

        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count

        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index

        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.start_page is not None:
            result['StartPage'] = self.start_page

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix

        if self.trim_policy_shrink is not None:
            result['TrimPolicy'] = self.trim_policy_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')

        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')

        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')

        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')

        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')

        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')

        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')

        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')

        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')

        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('Pages') is not None:
            self.pages = m.get('Pages')

        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')

        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')

        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')

        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')

        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')

        if m.get('TrimPolicy') is not None:
            self.trim_policy_shrink = m.get('TrimPolicy')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

