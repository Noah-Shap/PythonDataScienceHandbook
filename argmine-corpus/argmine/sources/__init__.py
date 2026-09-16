"""One module per metadata source. Every module exposes the same shape of
normalised record (see ``base.candidate``) so the phases never care where a
record came from, only which sources agree about it."""
