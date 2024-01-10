import re
from datetime import date


class PartialDate:
    def __init__(self, date_str):
        self.date_str = None if date_str in ["None", ""] else str(date_str)
        self.year = 0
        self.month = 0
        self.day = 0
        self.parse_date_str()

    def parse_date_str(self):
        pattern = re.compile(
            r"((?P<year>\d{4})(-(?P<month>\d{2})(?:-(?P<day>\d{1,2}))?)?)+"
            r"|" + r"(?:(?P<month_wy>\d{1,2})(-(?P<day_wy>\d{1,2}))?)$"
        )

        if self.date_str is None:
            self.year = 0
            self.month = 0
            self.day = 0
            return

        try:
            match = pattern.fullmatch(self.date_str or "")
            if match.groupdict()["year"] is not None:
                self.year = int(match.groupdict()["year"] or 0)
                self.month = int(match.groupdict()["month"] or 0)
                self.day = int(match.groupdict()["day"] or 0)
            else:
                self.year = int(match.groupdict()["year"] or 0)
                self.month = int(match.groupdict()["month_wy"] or 0)
                self.day = int(match.groupdict()["day_wy"] or 0)

        except:  # noqa: E722
            raise ValueError(
                "Invalid date format, valid formats are: 'None', YYYY-MM-DD, YYYY, YYYY-MM, MM or MM-DD."
                + f" date_str={self.date_str}, {type(self.date_str)}"
            )

        if self.day > 0 and self.month > 0:
            try:
                date(year=self.year or 2000, month=self.month, day=self.day)
            except ValueError as ve:
                raise ValueError(f"{ve}" + f", year={self.year} month={self.month} day={self.day}")

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def __len__(self):
        return len(self.__str__())
