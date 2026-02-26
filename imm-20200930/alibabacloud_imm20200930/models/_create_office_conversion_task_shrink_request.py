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
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The ending page for document conversion. The default value is -1, which converts the file until the last page of the file.
        # 
        # > 
        # 
        # *   If the source is a spreadsheet file, specify the index number of the corresponding sheet instead.
        # 
        # *   If you convert a large number of pages within the document, we recommend that you split the pages into several document conversion tasks to prevent conversion timeouts.
        # 
        # *   This parameter takes effect only when you convert the file into an image. It does not take effect when you convert the file into a PDF or TXT file.
        self.end_page = end_page
        # Specifies whether to return only the first resulting image when you convert a spreadsheet document to images. The number of rows and the number of columns in the first image are determined by the automatic splitting process. Valid values:
        # 
        # *   false (default): does not return only the first resulting image. All the resulting images are returned.
        # *   true: returns only the first resulting image. A thumbnail is generated.
        # 
        # >  This parameter takes effect only when the **LongPicture** parameter is set to `true`.
        self.first_page = first_page
        # Specifies whether to convert all rows of a spreadsheet document to one single image or a single-page PDF document when you convert the table document to an image or a PDF document. Valid values:
        # 
        # *   false (default): converts all rows of the document to multiple images or a multi-page PDF document. This is the default value.
        # *   true: converts all rows of the document to one single image or a single-page PDF document.
        self.fit_to_height = fit_to_height
        # Specifies whether to convert all columns of a spreadsheet document to one single image or a single-page PDF document when you convert the spreadsheet file to an image or a PDF document. Valid values:
        # 
        # *   false (default): converts all columns of the document to multiple images or a multi-page PDF document.
        # *   true: converts all columns of the document to one single image or a single-page PDF document.
        self.fit_to_width = fit_to_width
        # Specifies whether to retain line feeds in the output file when a document is converted to a text file. Valid values:
        # 
        # *   false (default): does not retain the line feeds.
        # *   true: retains the line feeds.
        self.hold_line_feed = hold_line_feed
        # The dots per inch (DPI) of output images. Valid values: 96 to 600. Default value: 96.
        self.image_dpi = image_dpi
        # Specifies whether to convert the document to a long image. Valid values:
        # 
        # *   false (default): does not convert the document to a long image.
        # *   true: converts the document to a long image.
        # 
        # >  You can convert up to 20 pages of a document into a long image. If you convert more than 20 pages to a long image, an error may occur.
        self.long_picture = long_picture
        # Specifies whether to convert the document to a long text file. Valid values:
        # 
        # *   false (default): does not convert the document to a long text file. Each page of the document is converted to a text file.
        # *   true: converts the entire document to a long text file.
        self.long_text = long_text
        # The maximum number of spreadsheet columns to be converted to an image. By default, all columns within the spreadsheet file are converted.
        # 
        # >  This parameter takes effect only when the **LongPicture** parameter is set to `true`.
        self.max_sheet_column = max_sheet_column
        # The maximum number of spreadsheet rows to be converted to an image. By default, all rows within the spreadsheet file are converted.
        # 
        # >  This parameter takes effect only when the **LongPicture** parameter is set to `true`.
        self.max_sheet_row = max_sheet_row
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The numbers of pages to be converted. This parameter takes precedence over the StartPage and EndPage parameters. The value of this parameter can be in different formats:
        # 
        # *   If you specify pages separately by page number, separate page numbers with commas (,). Example: 1,2
        # *   If you specify consecutive pages by using a page range, connect the starting and ending page numbers with a hyphen (-). Example: 1,2-4,7
        self.pages = pages
        # Specifies whether to place sheets of paper horizontally for converting a spreadsheet document to images. Conversion to images is similar to printing the content on a sheet of paper. Valid values:
        # 
        # *   false (default): does not place sheets of paper horizontally. Paper sheets are placed vertically.
        # *   true: places sheets of paper horizontally.
        self.paper_horizontal = paper_horizontal
        # The paper size for converting a spreadsheet document to images. Conversion to images is similar to printing the content on a sheet of paper. Valid values:
        # 
        # *   A0
        # *   A2
        # *   A4 (default)
        # 
        # >  This parameter takes effect only when the **FitToHeight** and **FitToWidth** parameters are specified.
        self.paper_size = paper_size
        # The password that protects the source document. To convert a password-protected document, specify this parameter.
        self.password = password
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The quality of the output file. Valid values: 0 to 100. A smaller value indicates lower quality and better conversion performance. By default, the system specifies an appropriate value that provides an optimal balance between the quality and conversion performance based on the document content.
        self.quality = quality
        # The percentage scale relative to the source document. Valid values: 20 to 199. The default value is 100, which indicates that the document is not scaled.
        # 
        # > A value that is less than 100 indicates a size reduction. A value that is greater than 100 indicates an enlargement.
        self.scale_percentage = scale_percentage
        # The number of sheets to be converted to an image. By default, all sheets within the spreadsheet file are converted.
        self.sheet_count = sheet_count
        # The index number of the sheet to be converted to an image. The value ranges from 1 to the index number of the last sheet. By default, the conversion starts from the first sheet.
        self.sheet_index = sheet_index
        # Specifies whether to display comments in resulting images when a text document is converted to images. Valid values:
        # 
        # *   false (default): does not display comments in resulting images.
        # *   true: displays comments in resulting images.
        self.show_comments = show_comments
        # The name extension of the source file. By default, the type of the source file is determined based on the name extension of the source object in OSS. If the object in OSS does not have a name extension, you can specify this parameter. Valid values:
        # 
        # *   Text documents: doc, docx, wps, wpss, docm, dotm, dot, dotx, and html
        # *   Presentation documents: pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss
        # *   Spreadsheet documents: xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets
        # *   PDF documents: pdf
        self.source_type = source_type
        # The URI of the source file.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        self.source_uri = source_uri
        # The list of images. The sequence of image URIs in the list determines the order in which they are converted. (**This parameter is not officially available and is not recommended.**)
        self.sources_shrink = sources_shrink
        # The starting page for document conversion. Default value: 1.
        # 
        # > 
        # 
        # *   If the document is a spreadsheet file, specify the index number of the corresponding sheet instead.
        # 
        # *   This parameter takes effect only when you convert the file to an image format. It does not take effect when you convert the file into a PDF or TXT file.
        self.start_page = start_page
        # The custom tags in dictionary format. You can use the custom tags to search for the task.
        self.tags_shrink = tags_shrink
        # The format of the output file. Valid values:
        # 
        # *   png: a PNG image.
        # *   jpg: a JPG image.
        # *   pdf: a PDF file.
        # *   txt: a TXT file. You can specify this value to extract the text content of the source document. Only presentation, text, or spreadsheet documents can be converted to a TXT file. If the source document is a spreadsheet, only one TXT is created and sheet-related parameters do not take effect.
        # 
        # This parameter is required.
        self.target_type = target_type
        # The address template of the output file.
        # 
        # Specify the value in the `oss://{bucket}/{tags.custom}/{dirname}/{barename}.{autoext}` format. For more information, see [TargetURI template](https://help.aliyun.com/document_detail/465762.html).
        # 
        # >  Specify at least one of the TargetURI and TargetURIPrefix parameters.
        self.target_uri = target_uri
        # The prefix of the storage address of the output file.
        # 
        # Specify the prefix in the `oss://${Bucket}/${Prefix}/` format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Prefix}` is the prefix of the output file.
        # 
        # >  Specify at least one of the TargetURI and TargetURIPrefix parameters.
        self.target_uriprefix = target_uriprefix
        # The trim policy for converting a spreadsheet file. Empty rows and columns may generate blank spaces in the output file if no appropriate trim policy is specified.
        self.trim_policy_shrink = trim_policy_shrink
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum information length is 2,048 bytes.
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

