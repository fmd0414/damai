from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Config:
    concert_keyword: str
    concert_detail_url: str | None
    smtp_host: str
    smtp_port: int
    smtp_user: str
    smtp_password: str
    email_to: str
    wechat_token: str
    wechat_provider: str  # "serverchan" or "pushplus"

def load_config() -> Config:
    return Config(
        concert_keyword=os.environ.get("CONCERT_KEYWORD", "刘宪华 苏州 演唱会"),
        concert_detail_url=os.environ.get("CONCERT_DETAIL_URL"),
        smtp_host=os.environ.get("SMTP_HOST", ""),
        smtp_port=int(os.environ.get("SMTP_PORT", "0") or 0),
        smtp_user=os.environ.get("SMTP_USER", ""),
        smtp_password=os.environ.get("SMTP_PASSWORD", ""),
        email_to=os.environ.get("EMAIL_TO", ""),
        wechat_token=os.environ.get("WECHAT_TOKEN", ""),
        wechat_provider=os.environ.get("WECHAT_PROVIDER", "serverchan"),
    )