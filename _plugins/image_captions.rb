# Wraps kramdown's `<p><img ... alt="..."></p>` output in a <figure> so the
# alt text can be shown as a centered caption below the image.
# Document hooks fire under their collection's own name (e.g. :articles,
# :entries), not a generic :documents bucket, so all collections are listed.
HOOK_OWNERS = [
  :pages, :posts, :documents, :articles, :entries, :photoindexes,
  :forteachers, :forguides, :forindividuals, :contributors,
].freeze

Jekyll::Hooks.register HOOK_OWNERS, :post_render do |doc|
  next unless doc.output_ext == ".html"

  doc.output = doc.output.gsub(
    /<p>\s*(<img\s+[^>]*?alt="([^"]*)"[^>]*?>)\s*<\/p>/
  ) do
    img_tag = Regexp.last_match(1)
    alt = Regexp.last_match(2)

    if alt.empty?
      "<p>#{img_tag}</p>"
    else
      "<figure class=\"article-figure\">#{img_tag}<figcaption>#{alt}</figcaption></figure>"
    end
  end
end
