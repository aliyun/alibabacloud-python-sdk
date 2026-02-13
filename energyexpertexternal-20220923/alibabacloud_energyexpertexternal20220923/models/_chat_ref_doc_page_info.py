# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatRefDocPageInfo(DaraModel):
    def __init__(
        self,
        angle: float = None,
        excel_parse_result: str = None,
        image_height: int = None,
        image_url: str = None,
        image_width: int = None,
        page_id_cur_doc: int = None,
        pdf_parse_result: str = None,
        word_parse_result: str = None,
    ):
        # The rotation angle of the image after the page is converted to an image.
        self.angle = angle
        # Reserved, can be unused for now.
        self.excel_parse_result = excel_parse_result
        # The height of the page turns to image.
        self.image_height = image_height
        # - The image URL after the page is converted to an image. 
        # - Note: The image URL will be inaccessible after 24 hours, so you need to save it promptly.
        self.image_url = image_url
        # The width of the page turns to image
        self.image_width = image_width
        # The page index in the current document, starting from 0.
        self.page_id_cur_doc = page_id_cur_doc
        # Reserved, can be unused for now.
        self.pdf_parse_result = pdf_parse_result
        # Reserved, can be unused for now.
        self.word_parse_result = word_parse_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['angle'] = self.angle

        if self.excel_parse_result is not None:
            result['excelParseResult'] = self.excel_parse_result

        if self.image_height is not None:
            result['imageHeight'] = self.image_height

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.image_width is not None:
            result['imageWidth'] = self.image_width

        if self.page_id_cur_doc is not None:
            result['pageIdCurDoc'] = self.page_id_cur_doc

        if self.pdf_parse_result is not None:
            result['pdfParseResult'] = self.pdf_parse_result

        if self.word_parse_result is not None:
            result['wordParseResult'] = self.word_parse_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('angle') is not None:
            self.angle = m.get('angle')

        if m.get('excelParseResult') is not None:
            self.excel_parse_result = m.get('excelParseResult')

        if m.get('imageHeight') is not None:
            self.image_height = m.get('imageHeight')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('imageWidth') is not None:
            self.image_width = m.get('imageWidth')

        if m.get('pageIdCurDoc') is not None:
            self.page_id_cur_doc = m.get('pageIdCurDoc')

        if m.get('pdfParseResult') is not None:
            self.pdf_parse_result = m.get('pdfParseResult')

        if m.get('wordParseResult') is not None:
            self.word_parse_result = m.get('wordParseResult')

        return self

