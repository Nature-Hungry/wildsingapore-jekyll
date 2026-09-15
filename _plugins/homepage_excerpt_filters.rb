module Jekyll
  module HomepageExcerptFilters
    def body_paragraph(input)
      return '' if input.nil?

      text = input.to_s

      text = text.gsub(/```.*?```/m, ' ')
      text = text.gsub(/!\[[^\]]*\]\([^)]*\)/, ' ')
      text = text.gsub(/\[[^\]]+\]\([^)]*\)/, ' ')
      text = text.gsub(/^\s*#+\s+.*$/m, "\n")
      text = text.gsub(/<\s*h[1-6][^>]*>.*?<\s*\/\s*h[1-6]\s*>/im, "\n")
      text = text.gsub(/<[^>]+>/, ' ')
      text = text.gsub(/\n{3,}/, "\n\n")

      paragraphs = text.split(/\n\s*\n+/)
      first_paragraph = paragraphs.map { |paragraph| paragraph.gsub(/\s+/, ' ').strip }
        .reject { |paragraph| paragraph.empty? || paragraph.start_with?('#') || paragraph.match?(/^(?:=+|-+)$/) }
        .first.to_s

      first_paragraph.split(/(?<=[.!?])\s+/).first.to_s
    end
  end
end

Liquid::Template.register_filter(Jekyll::HomepageExcerptFilters)
