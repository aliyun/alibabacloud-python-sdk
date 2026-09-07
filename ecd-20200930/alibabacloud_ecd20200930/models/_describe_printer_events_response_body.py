# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribePrinterEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribePrinterEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The user events.
        self.events = events
        # The pagination token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribePrinterEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePrinterEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        end_user_id: str = None,
        event_id: str = None,
        printer_driver: str = None,
        printer_job_copies: int = None,
        printer_job_name: str = None,
        printer_job_pages: int = None,
        printer_job_printed_pages: int = None,
        printer_job_size: int = None,
        printer_job_time: int = None,
        printer_name: str = None,
        printer_port: str = None,
        printer_redir_type: int = None,
    ):
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The end user ID.
        self.end_user_id = end_user_id
        # The event ID.
        self.event_id = event_id
        # The printer driver name.
        self.printer_driver = printer_driver
        # The number of copies to print.
        self.printer_job_copies = printer_job_copies
        # The print job name.
        self.printer_job_name = printer_job_name
        # The total number of pages in the print job.
        self.printer_job_pages = printer_job_pages
        # The number of printed pages.
        self.printer_job_printed_pages = printer_job_printed_pages
        # The print job size, in bytes.
        self.printer_job_size = printer_job_size
        # The print job time, in millisecond-precision UNIX timestamp.
        self.printer_job_time = printer_job_time
        # The printer name.
        self.printer_name = printer_name
        # The printer port.
        self.printer_port = printer_port
        # The printer redirection type.
        self.printer_redir_type = printer_redir_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.printer_driver is not None:
            result['PrinterDriver'] = self.printer_driver

        if self.printer_job_copies is not None:
            result['PrinterJobCopies'] = self.printer_job_copies

        if self.printer_job_name is not None:
            result['PrinterJobName'] = self.printer_job_name

        if self.printer_job_pages is not None:
            result['PrinterJobPages'] = self.printer_job_pages

        if self.printer_job_printed_pages is not None:
            result['PrinterJobPrintedPages'] = self.printer_job_printed_pages

        if self.printer_job_size is not None:
            result['PrinterJobSize'] = self.printer_job_size

        if self.printer_job_time is not None:
            result['PrinterJobTime'] = self.printer_job_time

        if self.printer_name is not None:
            result['PrinterName'] = self.printer_name

        if self.printer_port is not None:
            result['PrinterPort'] = self.printer_port

        if self.printer_redir_type is not None:
            result['PrinterRedirType'] = self.printer_redir_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('PrinterDriver') is not None:
            self.printer_driver = m.get('PrinterDriver')

        if m.get('PrinterJobCopies') is not None:
            self.printer_job_copies = m.get('PrinterJobCopies')

        if m.get('PrinterJobName') is not None:
            self.printer_job_name = m.get('PrinterJobName')

        if m.get('PrinterJobPages') is not None:
            self.printer_job_pages = m.get('PrinterJobPages')

        if m.get('PrinterJobPrintedPages') is not None:
            self.printer_job_printed_pages = m.get('PrinterJobPrintedPages')

        if m.get('PrinterJobSize') is not None:
            self.printer_job_size = m.get('PrinterJobSize')

        if m.get('PrinterJobTime') is not None:
            self.printer_job_time = m.get('PrinterJobTime')

        if m.get('PrinterName') is not None:
            self.printer_name = m.get('PrinterName')

        if m.get('PrinterPort') is not None:
            self.printer_port = m.get('PrinterPort')

        if m.get('PrinterRedirType') is not None:
            self.printer_redir_type = m.get('PrinterRedirType')

        return self

